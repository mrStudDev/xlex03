from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from typing import Any
from django.utils.text import slugify
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from app_manager .models import PageView

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    )

from .models import (
    CasoConcretoModel,
    DisciplinaCasosModel,
    RamoDireitoModel,
    TagCasoModel,
)

from .forms import (
    UpdateCasoForm,
    CreateCasoForm,
    )


class CasoConcretoView(ListView):
    model = CasoConcretoModel
    template_name = 'templates_casos/casos_list.html'
    ordering = ['-date_created']
    paginate_by = 12

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["publicacoes_count"] = CasoConcretoModel.objects.all().count()
        context["hide_sidebar"] = True
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Lista de Casos Page",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()
            
        return super().get(request, *args, **kwargs)


class CasoSingularView(DetailView):
    model = CasoConcretoModel
    template_name = 'templates_casos/caso_single.html'
    slug_field = 'slug'
    reverse_lazy = reverse_lazy('article-delete-post')    
    context_object_name = 'casos'

    def get(self, request, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        caso_name = self.object.title
        self.object.update_views()
        
        page, created = PageView.objects.get_or_create(
            page_name=f"Caso Post: {caso_name}",
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
        context['disciplinas'] = DisciplinaCasosModel.objects.all()
        context['ramos'] = RamoDireitoModel.objects.all()
        context['tags'] = TagCasoModel.objects.all()
        context['tagsx'] = TagCasoModel.objects.all()
        caso = self.get_object()
        context['tags'] = caso.tags.all()
        context['current_app'] = 'app_casos'  
        return context


class DisciplinaCasosView(ListView):
    model = CasoConcretoModel
    template_name = 'templates_casos/caso_disciplinas.html'
    context_object_name = 'casos'
    paginate_by = 12

    def get_queryset(self):
        self.disciplina = DisciplinaCasosModel.objects.get(slug=self.kwargs['disciplina_caso_slug'])
        return CasoConcretoModel.objects.filter(disciplina=self.disciplina)
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context.update({
            'disciplina': self.disciplina,
            'disciplinas': DisciplinaCasosModel.objects.all(),
            'ramos':RamoDireitoModel.objects.all(),
            'tags': TagCasoModel.objects.all(),
            'tagsx': TagCasoModel.objects.all(),
            'current_app': 'app_casos'
            
        })
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
        page_name=f"Casos: Diciplinas - {self.kwargs.get('disciplina_caso_slug', 'Unknown')}",
        defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)
    
    
class RamoDireitocasoViews(ListView):
    model = CasoConcretoModel
    template_name = 'templates_casos/caso_ramo_direito.html'
    context_object_name = 'casos'
    paginate_by = 12

    def get_queryset(self):
        self.ramo_direito = RamoDireitoModel.objects.get(slug=self.kwargs['ramo_caso_slug'])
        return CasoConcretoModel.objects.filter(ramo_direito=self.ramo_direito)
        
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update ({
            'ramo_direito': self.ramo_direito,
            'ramos': RamoDireitoModel.objects.all(),
            'disciplinas': DisciplinaCasosModel.objects.all(),
            'tagsx': TagCasoModel.objects.all(),
            'current_app': 'app_casos',
        })
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
    
        page, created = PageView.objects.get_or_create(
            page_name=f"Casos: Ramos do Direito - {self.kwargs.get('ramo_caso_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)
    
    
class TagCasosView(ListView):
    model = CasoConcretoModel
    template_name = 'templates_casos/casos_tags.html'
    context_object_name = 'casos'
    paginate_by = 12
    

    def get_queryset(self):
        self.tags = get_object_or_404(TagCasoModel, slug=self.kwargs['tagCaso_slug'])
        return CasoConcretoModel.objects.filter(tags=self.tags)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tags': self.tags,
            'tagsx': TagCasoModel.objects.all(),
            'disciplinas': DisciplinaCasosModel.objects.all(),
            'ramos': RamoDireitoModel.objects.all(),
            'current_app':  'app_casos' ,
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Casos: Tags - {self.kwargs.get('tagCaso_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


# Classes = Create, update e delete casos

class CasoCreateView(CreateView):
    model = CasoConcretoModel
    template_name = 'templates_casos/caso_create_post.html'
    form_class = CreateCasoForm
    success_url = reverse_lazy('app_casos:caso-single')
    
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(CasoCreateView, self).form_valid(form)
        return response
    
    def get_success_url(self):
        return reverse('app_casos:caso-single', kwargs={'slug': self.object.slug})
    
class UpdateCasoView(UpdateView):
    model = CasoConcretoModel
    form_class = UpdateCasoForm
    template_name = 'templates_casos/caso_update_post.html'
    success_url = reverse_lazy('app_casos:casos-list')
    
class CasoDeleteView(DeleteView):
    model = CasoConcretoModel
    template_name = 'templates_casos/caso_delete_post.html'
    success_url = reverse_lazy('app_casos:casos-list')