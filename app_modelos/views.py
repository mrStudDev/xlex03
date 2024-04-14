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
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from app_manager .models import PageView


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
        context["publicacoes_count"] = DocumentsModel.objects.all().count()
        context["hide_sidebar"] = True
        context['canonical_url'] = self.request.build_absolute_uri(reverse('app_modelos:modelos-list'))
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Modelos Docs Page",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()
            
        return super().get(request, *args, **kwargs)

class DocumentSingleView(DetailView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelo_single.html'
    ordering = ['-date_created']
    context_object_name = 'modelos'
    slug_field = 'slug'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        doc_name = self.object.title
        self.object.update_views()
        
        page, created = PageView.objects.get_or_create(
            page_name=f"Modelo Doc. Post: {doc_name}",
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
        context['ramo'] = RamoDireitoDocModel.objects.all()
        context['ramos'] = RamoDireitoDocModel.objects.all()
        context['tipo'] = TagDocumentsModel.objects.all()
        context['tags'] = TagDocumentsModel.objects.all()
        context['tagsx'] = TagDocumentsModel.objects.all()
        context['tipos'] = TipoDocumentModel.objects.all()
        context['current_app'] = 'app_modelos'
        modelos = self.get_object()
        context['indexable'] = modelos.is_indexable()
        context['canonical_url'] = self.request.build_absolute_uri(
            reverse('app_modelos:modelo-single', kwargs={'slug': self.object.slug})
        )
        return context


class RamoDocumentView(ListView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelos_ramo.html'
    context_object_name = 'modelos'
    paginate_by = 12
    
    def get_queryset(self):
        self.ramo_direito = RamoDireitoDocModel.objects.get(slug=self.kwargs['ramo_slug'])
        return DocumentsModel.objects.filter(ramo_direito=self.ramo_direito)


    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'ramo_direito': self.ramo_direito,
            'ramos': RamoDireitoDocModel.objects.all(),
            'tagsx': TagDocumentsModel.objects.all(),
            'tipos': TipoDocumentModel.objects.all(),
            'current_app': 'app_modelos',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    
        page, created = PageView.objects.get_or_create(
            page_name=f"Modelos: Ramos do Direito - {self.kwargs.get('ramo_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)
     

class TipoDocumentView(ListView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelos_tipo.html'
    context_object_name = 'modelos'
    
    def get_queryset(self):
        self.tipo_doc = TipoDocumentModel.objects.get(slug=self.kwargs['tipo_slug'])
        return DocumentsModel.objects.filter(tipo_doc=self.tipo_doc)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tipo_doc': self.tipo_doc,
            'tipos': TipoDocumentModel.objects.all(),
            'tags': TagDocumentsModel.objects.all(),
            'tagsx': TagDocumentsModel.objects.all(),
            'ramos': RamoDireitoDocModel.objects.all(),
            'current_app': 'app_modelos',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    
        page, created = PageView.objects.get_or_create(
            page_name=f"Modelos: Tipo de Doc - {self.kwargs.get('tipo_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


class TagDocumentView(ListView):
    model = DocumentsModel
    template_name = 'templates_modelos/modelos_tags.html'
    context_object_name = 'modelos'
    
    def get_queryset(self):
        self.tags = get_object_or_404(TagDocumentsModel, slug=self.kwargs['tag_slug'])
        return DocumentsModel.objects.filter(tags=self.tags)
        
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tags': self.tags,
            'tagsx': TagDocumentsModel.objects.all(),
            'tipos': TipoDocumentModel.objects.all(),
            'ramos': RamoDireitoDocModel.objects.all(),
            'current_app': 'app_modelos',
        })
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Modelos: Tags - {self.kwargs.get('tag_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


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