from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils.text import slugify
from typing import Any
from django.urls import reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )

from .models import (
    DocumentsModel,
    RamoDireitoDocModel,
    TipoDocumentModel,
    TagDocumentsModel,
)

from .forms import (
    CreateDocucumentForm,
    UpdateDocumentForm,
)


class DocumentListView(ListView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelos_list.html'
    ordering = ['-date_created']
    paginate_by = 12
    context_object_name = 'documents'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["hide_sidebar"] = True
        return context


class DocumentSingleView(DetailView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelo_single.html'
    ordering = ['-date_created']
    context_object_name = 'modelos'
    slug_field = 'slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Contagem das Visualizações
        self.object.update_views() 
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['ramo'] = RamoDireitoDocModel.objects.all()
        context['ramos'] = RamoDireitoDocModel.objects.all()
        context['tipo'] = TagDocumentsModel.objects.all()
        context['tags'] = TagDocumentsModel.objects.all()
        context['tagsx'] = TagDocumentsModel.objects.all()
        context['tipos'] = TipoDocumentModel.objects.all()
        context['current_app'] = 'app_modelos'
        return context


class RamoDocumentView(ListView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelos_ramo.html'
    context_object_name = 'modelos'
    
    def get_queryset(self):
        ramo_slug = self.kwargs['ramo_slug']
        ramo_direito = get_object_or_404(RamoDireitoDocModel, slug=ramo_slug)
        return DocumentsModel.objects.filter(ramo_direito=ramo_direito)


    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ramo_slug = self.kwargs['ramo_slug']
        context["ramo_direito"] = get_object_or_404(RamoDireitoDocModel, slug=ramo_slug)
        context['ramos'] = RamoDireitoDocModel.objects.all()
        context['tagsx'] = TagDocumentsModel.objects.all()
        context['tipos'] = TipoDocumentModel.objects.all()
        context['current_app'] = 'app_modelos'
        return context

class TipoDocumentView(ListView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelos_tipo.html'
    context_object_name = 'modelos'
    
    def get_queryset(self):
        tipo_slug = self.kwargs['tipo_slug']
        tipo_doc = get_object_or_404(TipoDocumentModel, slug=tipo_slug)
        return DocumentsModel.objects.filter(tipo_doc=tipo_doc)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tipo_slug = self.kwargs['tipo_slug']
        context["tipo_doc"] = get_object_or_404(TipoDocumentModel, slug=tipo_slug)
        context['tipos'] = TipoDocumentModel.objects.all()
        context['tagsx'] = TagDocumentsModel.objects.all()
        context['ramos'] = RamoDireitoDocModel.objects.all()
        context['current_app'] = 'app_modelos'
        return context


class TagDocumentView(ListView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelos_tags.html'
    context_object_name = 'modelos'
    
    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tags = get_object_or_404(TagDocumentsModel, slug=tag_slug)
        return DocumentsModel.objects.filter(tags=tags)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs['tag_slug']
        context["tags"] = get_object_or_404(TagDocumentsModel, slug=tag_slug)
        context['tagsx'] = TagDocumentsModel.objects.all()
        context['tipos'] = TipoDocumentModel.objects.all()
        context['ramos'] = RamoDireitoDocModel.objects.all()
        context['current_app'] = 'app_modelos'
        return context
    
    
# Classes - Formulários Create - Update - Delete

class CreateDocumentView(CreateView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelo_create.html'
    form_class = CreateDocucumentForm
    success_url = reverse_lazy('app_modelos:modelo-single')
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(CreateDocumentView, self).form_valid(form)
        return response
    
    def get_success_url(self):
        return reverse('app_modelos:modelo-single', kwargs={'slug': self.object.slug})

class UpdateModeloView(UpdateView):
    model = DocumentsModel
    form_class = UpdateDocumentForm
    template_name = 'templates_modelos/modelo_update.html'
    success_url = reverse_lazy('app_modelos:modelos-list')


class DeleteModeloView(DeleteView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelo_delete.html'
    success_url = reverse_lazy('app_modelos:modelos-list')