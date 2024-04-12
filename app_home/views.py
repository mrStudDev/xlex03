from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.shortcuts import render, redirect
from typing import Any
from .models import HomeSite
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.utils import timezone
from django.views.generic import TemplateView

from app_manager .models import PageView
from .forms import ContactForm

class XlexHomeView(ListView):
    model = HomeSite
    template_name = 'index.html'
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        # Lógica para registrar acesso usando PageView
        page, created = PageView.objects.get_or_create(
            page_name="Home Page",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        # Chama a implementação base para continuar com o fluxo normal da view
        return super().get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        # Chama a implementação base primeiro para obter um contexto
        context = super().get_context_data(**kwargs)
        
        # Obtém o objeto HomeSite
        home_site_object = HomeSite.objects.first()
        
        if home_site_object:
            home_site_object.update_views()   # Aumenta as visualizações diretamente
            context['home_site'] = home_site_object  # Adiciona o objeto HomeSite ao contexto
        else:
            context['home_site'] = None
        
        # Adiciona outras variáveis ao contexto
        context["hide_navbar"] = True
        context['canonical_url'] = self.request.build_absolute_uri(reverse('app_home:home-view'))
        return context

# Páginas do Site (sobre, contato, paginas de listas, etc)

def sobre_nos(request):
    return render(request, 'sobre_nos.html', {'hide_sidebar':True})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a mensagem no banco de dados
            return render(request, 'contact_us.html', {'form': ContactForm(), 'success': True, 'hide_sidebar': True,})
    else: # Redireciona para uma URL de sucesso
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form, 'hide_sidebar': True,})


class JurisprudenciasListView(TemplateView):
    template_name = 'jurisprudencias.html'

    def get(self, request, *args, **kwargs):
        # Lógica para registrar acesso usando PageView
        page, created = PageView.objects.get_or_create(
            page_name="Jurisprudências Cards-Tribunais",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        # Agora, construa o contexto manualmente aqui, pois você está em TemplateView
        context = {'hide_sidebar': True}
        # Adicione mais contexto conforme necessário
        return self.render_to_response(context)
