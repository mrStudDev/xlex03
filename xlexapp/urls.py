"""
URL configuration for xlexapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')),
    path('manager/', include('app_manager.urls')),
    path('jurisprudencias-stj/', include('app_juris_stj.urls')),
    path('sumulas/', include('app_sumulas.urls')),
    path('searchs/', include('app_searchs.urls')),
    path('principios/', include('app_principios.urls')),
    path('questions/', include('app_questions.urls')),
    path('casos/', include('app_casos.urls')),
    path('modelos/', include('app_modelos.urls')),
    path('artigos/', include('app_articles.urls')),
    path('educacao-social/', include('app_edu_social.urls')),
    path("robots.txt", RedirectView.as_view(url=staticfiles_storage.url("seo/robots.txt")), name="robots_file"),
    path("sitemap.xml", RedirectView.as_view(url=staticfiles_storage.url("seo/sitemap.xml")), name="sitemap_file"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)