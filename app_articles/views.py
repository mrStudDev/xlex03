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
    CategoryArticlesModel,
    TagArticlesModel,
    ArticlesModel,
)

from .forms import (
    CreateArticleForm,
    UpdateArticleForm,
    )


class ArticlesListView(ListView):
    model = ArticlesModel
    template_name = 'templates_articles/articles_list.html'
    ordering = ['-date_created']
    paginate_by = 12
    context_object_name = 'articles'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["publicacoes_count"] = ArticlesModel.objects.all().count()
        context["hide_sidebar"] = True
        context['canonical_url'] = self.request.build_absolute_uri(reverse('app_articles:articles-list'))
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name="Lista de Artigos",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


class ArticleSingleView(DetailView):
    model = ArticlesModel
    template_name = 'templates_articles/article_single.html'
    slug_field = 'slug'
    reverse_lazy = reverse_lazy('article-delete-post')
    context_object_name = 'articles'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        article_name = self.object.title
        self.object.update_views()
        
        page, created = PageView.objects.get_or_create(
            page_name=f"Article Post: {article_name}",
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
        context['categories'] = CategoryArticlesModel.objects.all()
        context['tagsx'] = TagArticlesModel.objects.all()
        articles = self.get_object()
        context['tags'] = articles.tags.all()
        context['current_app'] = 'app_articles'
        context['canonical_url'] = self.request.build_absolute_uri(reverse('app_articles:article-single', kwargs={'slug': self.object.slug}))
        return context

class CategoryListView(ListView):
    model = ArticlesModel  
    template_name = 'templates_articles/categories.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.category = CategoryArticlesModel.objects.get(slug=self.kwargs['category_slug'])
        return ArticlesModel.objects.filter(category=self.category)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'category': self.category,
            'categories': CategoryArticlesModel.objects.all(),
            'tagsx': TagArticlesModel.objects.all(),
            'current_app': 'app_articles',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Article: Categorias - {self.kwargs.get('category_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


class TagArticlesView(ListView):
    model = ArticlesModel
    template_name = 'templates_articles/article_tags.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.tag = get_object_or_404(TagArticlesModel, slug=self.kwargs['tagArticle_slug'])
        return ArticlesModel.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'tag': self.tag,
            'categories': CategoryArticlesModel.objects.all(),
            'tagsx': TagArticlesModel.objects.all(),
            'current_app': 'app_articles',
        })
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        page, created = PageView.objects.get_or_create(
            page_name=f"Article: Tags - {self.kwargs.get('tagArticle_slug', 'Unknown')}",
            defaults={'last_accessed': timezone.now()}
        )
        if not created:
            page.view_count += 1
            page.last_accessed = timezone.now()
            page.save()

        return super().get(request, *args, **kwargs)


# Classes = Create, Update e delete Articles

class CreateArticleView(CreateView):
    model = ArticlesModel
    template_name = 'templates_articles/article_create_post.html'
    form_class = CreateArticleForm
    success_url = reverse_lazy('app_articles:article-single') 

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(CreateArticleView, self).form_valid(form)
        return response
    
    def get_success_url(self):
        return reverse('app_articles:article-single', kwargs={'slug': self.object.slug})
    
class UpdateArticleView(UpdateView):
    model = ArticlesModel
    form_class = UpdateArticleForm
    template_name = 'templates_articles/article_update_post.html'
    success_url = reverse_lazy('app_articles:articles-list')

class DeleteArticleView(DeleteView):
    model = ArticlesModel
    template_name = 'templates_articles/article_delete_post.html'
    success_url = reverse_lazy('app_articles:articles-list')
    
