from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from typing import Any
from django.db.models import Sum
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from app_manager .models import PageView

from .forms import (
    CreateXlexQuestionForm,
    CreateXlexAnswerForm,
)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import (
    XlexQuestionModel,
    BancaQuestionModel,
    DisciplinaQuestionModel,
    RamoDireitoQuestionModel,
    TagQuestionModel,
    AlternativasModel,
    )


class XlexQuestionView(ListView):
    model = XlexQuestionModel
    template_name = 'templates_questions/questions_list.html'
    ordering = ['-date_created']
    paginate_by = 12
    context_object_name = 'questions'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["publicacoes_count"] = XlexQuestionModel.objects.all().count()
        context["hide_sidebar"] = True
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Lista de Questões",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)

class QuestionSingularView(DetailView):
    model = XlexQuestionModel
    template_name = 'templates_questions/question_single.html'
    slug_field = 'slug'
    context_object_name = 'questions'
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        question_name = self.object.title
        self.object.update_views()

        page, created = PageView.objects.get_or_create(
            page_name=f"Question Post: {question_name}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()
        
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['bancas'] = BancaQuestionModel.objects.all()
        context['disciplinas'] = DisciplinaQuestionModel.objects.all()
        context['ramos'] = RamoDireitoQuestionModel.objects.all()
        context['tagsx'] = TagQuestionModel.objects.all()
        # Pega a questão atual - Tags
        question = self.get_object()
        context['tags'] = question.tags.all()
        context['current_app'] = 'app_questions'
        return context


class BancaQuestionView(ListView):
    model = XlexQuestionModel
    template_name = 'templates_questions/question_banca.html'
    context_object_name = 'questions'

    def get_queryset(self):
        self.banca = BancaQuestionModel.objects.get(slug=self.kwargs['banca_slug'])
        return XlexQuestionModel.objects.filter(banca=self.banca)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'banca': self.banca,
            "bancas": BancaQuestionModel.objects.all(),
            "disciplinas": DisciplinaQuestionModel.objects.all(),
            "ramos": RamoDireitoQuestionModel.objects.all(),
            "tagsx": TagQuestionModel.objects.all(),
            "current_app": 'app_questions',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Question: Bancas - {self.kwargs.get('banca_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)

class DiciplinaQuestionView(ListView):
    model = XlexQuestionModel
    template_name = 'templates_questions/question_disciplina.html'
    context_object_name = 'questions'

    def get_queryset(self):
        self.disciplina = DisciplinaQuestionModel.objects.get(slug=self.kwargs['disciplina_slug'])
        return XlexQuestionModel.objects.filter(disciplina=self.disciplina)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'disciplina': self.disciplina,
            'disciplinas': DisciplinaQuestionModel.objects.all(),
            'ramos': RamoDireitoQuestionModel.objects.all(),
            'bancas': BancaQuestionModel.objects.all(),
            'tagsx': TagQuestionModel.objects.all(),
            'current_app': 'app_questions',
        })     
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Questions: Disciplinas - {self.kwargs.get('disciplina_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)

class RamoDireitoQuestionView(ListView):
    model = XlexQuestionModel
    template_name = 'templates_questions/question_ramo_direito.html'
    context_object_name = 'questions'

    def get_queryset(self):
        self.ramo_direito = RamoDireitoQuestionModel.objects.get(slug=self.kwargs['ramo_slug'])
        return XlexQuestionModel.objects.filter(ramo_direito=self.ramo_direito)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'context': self.ramo_direito,
            'ramo': RamoDireitoQuestionModel.objects.all(),
            'ramos': RamoDireitoQuestionModel.objects.all(),
            'bancas': BancaQuestionModel.objects.all(),
            'tagsx': TagQuestionModel.objects.all(),
            'disciplinas': DisciplinaQuestionModel.objects.all(),
            'current_app': 'app_questions',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Questions: Ramos do Direito - {self.kwargs.get('ramo_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)    


class TagQuestionView(ListView):
    model = XlexQuestionModel
    template_name = 'templates_questions/question_tags.html'
    context_object_name = 'questions'

    def get_queryset(self):
        self.tag = get_object_or_404(TagQuestionModel, slug=self.kwargs['tagQuestion_slug'])
        return XlexQuestionModel.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tag': self.tag,
            'tags': TagQuestionModel.objects.all(),
            'tagsx': TagQuestionModel.objects.all(),
            'bancas': BancaQuestionModel.objects.all(),
            'ramos': RamoDireitoQuestionModel.objects.all(),
            'disciplinas': DisciplinaQuestionModel.objects.all(),
            'current_app': 'app_questions',
        })
        return context


# Autenticação Staff
def is_superuser_or_staff(user):
    return user.is_superuser or user.is_staff


# Class Função Required Login Staff
class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        if not request.user.is_staff:
            return HttpResponseForbidden()
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Formulários Create
# Create Question
@method_decorator(csrf_exempt, name='dispatch')
class CreateXlexQuestionView(StaffRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        questao_x_id = kwargs.get('questao_x_id', None)
        form = CreateXlexQuestionForm()
        return render(request, 'templates_questions/question_create.html', {'form': form, 'questao_x_id': questao_x_id})

    def post(self, request, *args, **kwargs):
        form = CreateXlexQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('app_questions:question-create-answer', questao_x_id=question.id)

        else:
            print(" This form is not valid")
            return render(request, 'templates_questions/question_create.html', {'form': form})


# Create Answer
@method_decorator(csrf_exempt, name='dispatch')
class CreateAnswerView(StaffRequiredMixin, View):
    def get(self, request, questao_x_id):
        form = CreateXlexAnswerForm(initial={'question': questao_x_id})
        question = XlexQuestionModel.objects.get(id=questao_x_id)
        question_ask = question.question_ask

        # Recupere as alternativas associadas a esta questão
        recent_answers = AlternativasModel.objects.filter(question=question)
        return render(request, 'templates_questions/question_answer_create.html', {'form': form, 'questao_x_id': questao_x_id, 'question_ask': question_ask, 'recent_answers': recent_answers})

    def post(self, request, questao_x_id):
        form = CreateXlexAnswerForm(request.POST)
        if form.is_valid():
            ansewer = form.save()
            return redirect('app_questions:question-create-answer', questao_x_id=questao_x_id)

        else:
            print(form.errors)   
            return render(request, 'templates_questions/question_answer_create.html', {'form': form})

def get_full_question_text(request, questao_x_id):
    try:
        question = XlexQuestionModel.objects.get(pk=questao_x_id)
        return JsonResponse({'question_ask': question.question_ask})
    except XlexQuestionModel.DoesNotExist:
        return JsonResponse({'error': 'Question Not Found'}, status=404)