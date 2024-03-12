from app_juris_stj.models import STJjurisprudenciaModel
from app_sumulas.models import SumulaModel
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UniversalSearchForm, AdvancedSearchForm, SumulaSearchForm
from .adapters.juris_stj_adapter import JurisSTJSearchAdapter, AdvancedJurisSTJSearchAdapter
from django.contrib.postgres.search import SearchVector, SearchQuery
import re
from datetime import datetime
from django.db.models import Min, Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from app_manager .models import PageView


def universal_search_view(request):
    search_performed = False
    results = []
    
    if request.GET.get('query'):
        search_performed = True
    form = UniversalSearchForm(request.GET or None)

    all_results = []
    vector = []

    if form.is_valid():
        search_performed = True
        query_string = form.cleaned_data.get('query')
        
        vector = SearchVector('ementa')
        search_query = SearchQuery(query_string)

        # Passamos os parâmetros da busca para o adaptador.
        i_results = STJjurisprudenciaModel.objects.annotate(search=vector).filter(search=search_query)
        results = JurisSTJSearchAdapter.search(ementa=query_string)
        all_results.extend(results)
        for item in all_results:
            item.snippet = generate_snippet(item.ementa, query_string)

    results_per_page = 20  # ou qualquer outro número que você quiser
    paginator = Paginator(results, results_per_page)

    page = request.GET.get('page')

    try:
        paged_results = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, entrega a primeira página.
        paged_results = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do alcance (por exemplo, 9999), entrega a última página de resultados.
        paged_results = paginator.page(paginator.num_pages)

    return render(request, 'templates_search/universal_results.html', {
        'form': form,
        'results': all_results,
        'vector': vector,
        'search_performed': search_performed,
        'results': paged_results,
    })


def advanced_search_view(request):
    queryset = STJjurisprudenciaModel.objects.all()
    search_performed = False
    form = AdvancedSearchForm(request.POST or None)  

    # Se a requisição for POST, processa o formulário
    if request.method == 'POST':
        search_performed = True
        # Captura os valores dos campos do formulário
        ementa = request.POST.get('ementa', '')
        data_inicial = request.POST.get('data_inicial')
        data_final = request.POST.get('data_final')
        descricaoClasse = request.POST.get('descricaoClasse', '')
        numeroProcesso = request.POST.get('numeroProcesso', '')
        ministroRelator = request.POST.get('ministroRelator', '')

        # Faz a filtragem dos resultados no banco de dados
        results = STJjurisprudenciaModel.objects.all()
        
        if ementa:
            results = results.filter(ementa__icontains=ementa)
        if data_inicial and data_final:
            results = results.filter(data_formatada__range=(data_inicial, data_final))
        if descricaoClasse:
            results = results.filter(descricaoClasse__icontains=descricaoClasse)
        if numeroProcesso:
            results = results.filter(numeroProcesso__icontains=numeroProcesso)
        if ministroRelator:
            results = results.filter(ministroRelator__icontains=ministroRelator)

        request.session['search_results'] = list(results.values())
        search_performed = bool(request.GET)
        # Redireciona para a página de resultados
        serialized_results = []

        for result in results:
            result_dict = result.__dict__.copy()  # Crie uma cópia para não modificar o objeto original
            result_dict['data_formatada'] = result.data_formatada.strftime('%Y-%m-%d')
            
            # Removendo o atributo problemático
            result_dict.pop('_state', None)
            
            serialized_results.append(result_dict)

        request.session['search_results'] = serialized_results


        return redirect('app_searchs:advanced-results-view')
    else:
        total_records = STJjurisprudenciaModel.objects.all().count()
        date_range = STJjurisprudenciaModel.objects.aggregate(Min('data_formatada'), Max('data_formatada'))
        earliest_date = date_range['data_formatada__min']
        latest_date = date_range['data_formatada__max']
        return render(request, 'templates_search/advanced_search_view.html', {'total_records': total_records,'earliest_date': earliest_date,'latest_date': latest_date, 'hide_sidebar': True,})
    
    

def advanced_results_view(request):
    # Lógica para atualizar a contagem de visualizações
    page_stj, created = PageView.objects.get_or_create(
        page_name="Resultado Pesquisa Jurisprudência STJ",
        defaults={'last_accessed': timezone.now()}
    )
    if not created:
        page_stj.view_count += 1
        page_stj.last_accessed = timezone.now()
        page_stj.save()

    # Processamento dos resultados serializados da sessão
    serialized_results = request.session.get('search_results', [])
    results = []
    for result_dict in serialized_results:
        result = STJjurisprudenciaModel(**result_dict)
        result.data_formatada = datetime.strptime(result_dict['data_formatada'], '%Y-%m-%d').date()
        results.append(result)

    # Configuração da paginação
    results_per_page = 20
    paginator = Paginator(results, results_per_page)
    page_number = request.GET.get('page')

    try:
        paged_results = paginator.page(page_number)
    except PageNotAnInteger:
        paged_results = paginator.page(1)
    except EmptyPage:
        paged_results = paginator.page(paginator.num_pages)

    # Renderização do template com os resultados paginados
    return render(request, 'templates_search/advanced_results_view.html', {
        'results': paged_results,  # Certifique-se de que o template use 'results' para iterar
        'search_performed': True,
        'hide_sidebar': True,
    })



def sumula_search_view(request):
    page, created = PageView.objects.get_or_create(
        page_name="Resultados de Pesquisa Súmulas",
        defaults={'last_accessed': timezone.now()}
    )
    if not created:
        page.view_count += 1
        page.last_accessed = timezone.now()
        page.save()
        
    if request.method == 'POST':
        form = SumulaSearchForm(request.POST)
        search_performed = True
    else:
        # Passa um dicionário com strings vazias para inicializar os campos, assim os placeholders serão mostrados.
        initial_data = {field: '' for field in SumulaSearchForm.Meta.fields}
        form = SumulaSearchForm(initial=initial_data)
        search_performed = False

    sum_results = SumulaModel.objects.all()
    total_records = SumulaModel.objects.all().count()

    if search_performed:
        enunciado = request.POST.get('enunciado', '')
        sigla_tribunal = request.POST.get('sigla_tribunal', '')
        numero_sumula = request.POST.get('numero_sumula', '')
        tema_juridico = request.POST.get('tema_juridico', '')
        nome_tribunal = request.POST.get('nome_tribunal', '')

        if enunciado:
            sum_results = sum_results.filter(enunciado__icontains=enunciado)
        if sigla_tribunal:
            sum_results = sum_results.filter(sigla_tribunal__name__icontains=sigla_tribunal)
        if numero_sumula:
            sum_results = sum_results.filter(numero_sumula__icontains=numero_sumula)
        if tema_juridico:
            sum_results = sum_results.filter(tema_juridico__icontains=tema_juridico)
        if nome_tribunal:
            sum_results = sum_results.filter(nome_tribunal__name__icontains=nome_tribunal)

    return render(request, 'templates_search/sumula_search_view.html', {
        'form': form,
        'sum_results': sum_results, 
        'total_records': total_records, 
        'search_performed': search_performed, 
        'hide_sidebar': True,
    })



def generate_snippet(text, keyword, length=130):
    # Encontra a posição da palavra-chave no texto
    index = text.lower().find(keyword.lower())
    
    # Se a palavra-chave não for encontrada, retorne um snippet vazio
    if index == -1:
        return ""

    # Determine os pontos de início e fim do snippet
    start = max(0, index - length)
    end = min(len(text), index + length + len(keyword))

    # Extraia o snippet
    snippet = text[start:end]

    # Substitua a palavra-chave no snippet para destacá-la (isso é opcional e pode ser ajustado conforme necessário)
    highlighted = "<strong>" + keyword + "</strong>"
    #snippet = snippet.replace(keyword, highlighted, 1)
    snippet = re.sub(re.escape(keyword), highlighted, snippet, flags=re.I)

    return snippet






