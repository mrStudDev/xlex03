from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from typing import Any
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.aggregates import Count
from random import randint
from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from app_manager .models import PageView

from django.views.generic import (
    ListView,
    DateDetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import (
    PrincipiosModel,
    RamoDireitoModel,
)

class PrincipiosListView(ListView):
    model = PrincipiosModel
    template_name = 'templates_principios/principios_list.html'
    ordering = ['-date_created']
    paginate_by = 12
    context_object_name = 'principios'
    
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['publicacoes_count'] = PrincipiosModel.objects.all().count()
        context["hide_sidebar"] = True
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Lista de Princípios",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)

class PrincipiosSingleView(DeleteView):
    model = PrincipiosModel
    template_name = 'templates_principios/principio_single.html'
    slug_field = 'slug'
    context_object_name = 'principios'
    reverse_lazy = reverse_lazy('app_principios:principios-list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        principio_Direitoname = self.object.principio_name
        self.object.update_views() 
        
        page, created = PageView.objects.get_or_create(
            page_name=f"Principio post: {principio_Direitoname}",
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
        context['ramos'] = RamoDireitoModel.objects.all()
        context['current_app'] = 'app_principios'
        return context
    
class RamoDireitoListView(ListView):
    model = RamoDireitoModel
    template_name = 'templates_principios/principios_ramos_list.html'
    context_object_name = 'principios'
    
    def get_queryset(self):
        self.ramo = RamoDireitoModel.objects.get(slug=self.kwargs['ramo_slug'])
        return PrincipiosModel.objects.filter(ramo_direito=self.ramo)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'ramo': self.ramo,
            'ramos': RamoDireitoModel.objects.all(),
            'current_app': 'app_principios',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Principios: Ramos do Direito - {self.kwargs.get('ramo_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)