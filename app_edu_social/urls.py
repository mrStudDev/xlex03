from django.urls import path
from . views import (
    ArticlesSocialListView,
    ArticleSocialSingleView,
    CategorySocialListView,
    TagArticlesSocialView,
    CreateSocialArticleView,
    UpdateSocialArticleView,
    DeleteSocialArticleView,
  )
from . import views

app_name = 'app_edu_social'

urlpatterns = [
  path('', ArticlesSocialListView.as_view(), name='articles-social-list'),
  path('post/<slug:slug>/', ArticleSocialSingleView.as_view(), name='article-social-single'),
  path('categorias/<slug:category_slug>/', CategorySocialListView.as_view(), name='categories-social-articles'),  
  path('tags/<slug:tagArticle_slug>/', TagArticlesSocialView.as_view(), name='tags-social-articles'),
  path('article-create/', CreateSocialArticleView.as_view(), name='article-social-create'),
  path('article-update/<slug:slug>/', UpdateSocialArticleView.as_view(), name='article-social-update'),
  path('article-delete/<slug:slug>/', DeleteSocialArticleView.as_view(), name='article-social-delete'),
]