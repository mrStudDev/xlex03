from django.urls import path
from . views import (
  ArticlesListView, 
  ArticleSingleView, 
  CategoryListView, 
  TagArticlesView,
  CreateArticleView,
  UpdateArticleView,
  DeleteArticleView,
  )
from . import views

app_name = 'app_articles'

urlpatterns = [
  path('', ArticlesListView.as_view(), name='articles-list'),
  path('post/<slug:slug>/', ArticleSingleView.as_view(), name='article-single'),
  path('categorias/<slug:category_slug>/', CategoryListView.as_view(), name='categories-articles'),  
  path('tags/<slug:tagArticle_slug>/', TagArticlesView.as_view(), name='tags-articles'),
  path('article-create/', CreateArticleView.as_view(), name='article-create-post'),
  path('article-update/<slug:slug>/', UpdateArticleView.as_view(), name='article-update-post'),
  path('article-delete/<slug:slug>/', DeleteArticleView.as_view(), name='article-delete-post'),
]