from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.urls import reverse
from django.db.models import Q
from typing import Any
from django.utils.text import slugify
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from app_manager .models import PageView

from .models import (
    SumulaModel,
    TribNameSumulaModel,
    SiglaTribSumulaModel,
    )

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

from .forms import (
    CreateSumulaForm,
    UpdateSumulaForm,
)

class SumulasListView(ListView):
    model = SumulaModel
    template_name = 'templates_sumulas/sumulas_list.html'
    ordering = ['-date_created']
    paginate_by = 12
    context_object_name = 'sumulas'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["publicacoes_count"] = SumulaModel.objects.all().count()
        context["hide_sidebar"] = True
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Lista de Súmulas",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)

class SumulaSingularView(DetailView):
    model = SumulaModel
    template_name = 'templates_sumulas/sumula_single.html'
    slug_field = 'slug'
    slug_url_kwarg = 'sumula_slug'
    context_object_name = 'sumulas'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        sumula_name = self.object.title
        self.object.update_views()
        
        page, created = PageView.objects.get_or_create(
            page_name=f"Súmula Post: {sumula_name}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()
            
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hide_sidebar"] = True
        sumulas = self.get_object()
        context['current_app'] = 'app_sumulas'
        return context

class TribNameSumulaView(ListView):
    model = TribNameSumulaModel
    template_name = 'templates_sumulas/sumulas_trib_names.html'
    context_object_name = 'sumulas'
    
    def get_queryset(self):
        self.tribunaisSum = TribNameSumulaModel.objects.get(slug=self.kwargs['tribNameSum_slug'])
        return SumulaModel.objects.filter(tribunaisSum=self.tribunaisSum)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tribunaisSum': self.tribunaisSum,
            'tribunaisSums': TribNameSumulaModel.objects.all(),
            'siglaTribSumula': SiglaTribSumulasView.objects.all(),
            'current_app': 'app_sumulas',
        })
        return context


class SiglaTribSumulasView(ListView):
    model = TribNameSumulaModel
    template_name = 'templates_sumulas/sumulas_trib_siglas.html'
    context_object_name = 'sumulas'
    
    def get_queryset(self):
        self.siglaTribSumula = SiglaTribSumulaModel.objects.get(slug=self.keargs['siglaTrib_slug'])
        return SumulaModel.objects.filter(siglaTribSumula=self.siglaTribSumula)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'siglaTribSumula': self.siglaTribSumula,
            'siglaTribSumulas': SiglaTribSumulasView.objects.all(),
            'tribunaisSums': TribNameSumulaModel.objects.all(),
            'current_app': 'app_sumulas',
        })
        return context   
    
# Classes Create; 

class CreateSumulaView(CreateView):
    model = SumulaModel
    template_name = 'templates_sumulas/sumula_create_post.html'
    form_class = CreateSumulaForm
    success_url = reverse_lazy('app_sumulas:sumula-single')
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(CreateSumulaView, self).form_valid(form)
        return response
    
    def get_success_url(self):
        return reverse('app_sumulas:sumula-single', kwargs={'sumula_slug': self.object.slug})

class UpdateSumulaView(UpdateView):
    model = SumulaModel
    template_name = 'templates_sumulas/sumula_update_post.html'
    form_class = UpdateSumulaForm
    success_url = reverse_lazy('app_sumulas:sumulas-list')
    

class DeleteSumulaView(DeleteView):
    model = SumulaModel
    template_name = 'templates_sumulas/sumula_delete_post.html'
    success_url = reverse_lazy('app_sumulas:sumulas-list')