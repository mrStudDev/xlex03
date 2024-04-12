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
from django.db.models import Sum
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
    CategorySocialModel,
    TagSocialModel,
    ArticlesSocialModel
)
from .forms import (
    CreateArticleSocialForm,
    UpdateArticleSocialForm,
    )


class ArticlesSocialListView(ListView):
    model = ArticlesSocialModel
    template_name = 'templates_social/articles_social_list.html'
    ordering = ['-date_created']
    paginate_by = 12
    context_object_name = 'social'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["publicacoes_count"] = ArticlesSocialModel.objects.all().count()
        context["hide_sidebar"] = True
        context['canonical_url'] = self.request.build_absolute_uri(reverse('app_edu_social:articles-social-list'))
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Lista de Artigos Social",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


class ArticleSocialSingleView(DetailView):
    model = ArticlesSocialModel
    template_name = 'templates_social/article_social_single.html'
    slug_field = 'slug'
    reverse_lazy = reverse_lazy('article-social-delete')
    context_object_name = 'social'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        article_name = self.object.title
        self.object.update_views()
        
        page, created = PageView.objects.get_or_create(
            page_name=f"Article Social Post: {article_name}",
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
        context['categories'] = CategorySocialModel.objects.all()
        context['tagsx'] = TagSocialModel.objects.all()
        social = self.get_object()
        context['tags'] = social.tags.all()
        context['current_app'] = 'app_edu_social'
        context['canonical_url'] = self.request.build_absolute_uri(
            reverse('app_edu_social:article-social-single', kwargs={'slug': self.object.slug})
        )
        return context

class CategorySocialListView(ListView):
    model = ArticlesSocialModel  
    template_name = 'templates_social/categories.html'
    context_object_name = 'social'

    def get_queryset(self):
        self.category = CategorySocialModel.objects.get(slug=self.kwargs['category_slug'])
        return ArticlesSocialModel.objects.filter(category=self.category)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'category': self.category,
            'categories': CategorySocialModel.objects.all(),
            'tagsx': TagSocialModel.objects.all(),
            'current_app': 'app_edu_social',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Article-Social: Categorias - {self.kwargs.get('category_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)

class TagArticlesSocialView(ListView):
    model = ArticlesSocialModel
    template_name = 'templates_social/article_social_tags.html'
    context_object_name = 'social'

    def get_queryset(self):
        self.tag = get_object_or_404(TagSocialModel, slug=self.kwargs['tagArticle_slug'])
        return ArticlesSocialModel.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tag': self.tag,
            'categories': CategorySocialModel.objects.all(),
            'tagsx': TagSocialModel.objects.all(),
            'current_app': 'app_edu_social',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Article-social: Tags - {self.kwargs.get('tagArticle_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)
    
# Classes = Create, Update e delete Articles SOCIAL

class CreateSocialArticleView(CreateView):
    model = ArticlesSocialModel
    template_name = 'templates_social/article_social_create.html'
    form_class = CreateArticleSocialForm
    success_url = reverse_lazy('app_edu_social:article-social-single') 

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(CreateSocialArticleView, self).form_valid(form)
        return response
    
    def get_success_url(self):
        return reverse('app_edu_social:article-social-single', kwargs={'slug': self.object.slug})

class UpdateSocialArticleView(UpdateView):
    model = ArticlesSocialModel
    form_class = UpdateArticleSocialForm
    template_name = 'templates_social/article_social_update.html'
    success_url = reverse_lazy('app_edu_social:articles-social-list')

class DeleteSocialArticleView(DeleteView):
    model = ArticlesSocialModel
    template_name = 'templates_social/article_social_delete.html'
    success_url = reverse_lazy('app_edu_social:articles-social-list')
    
