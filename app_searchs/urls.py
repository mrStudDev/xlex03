from django.urls import path

from . import views

app_name = 'app_searchs'

urlpatterns = [
    path('', views.universal_search_view, name='universal-searchs-results'),
    path('advanced/', views.advanced_search_view, name='advanced-searchs-view'),
    path('advanced-results/', views.advanced_results_view, name='advanced-results-view'),

    path('sumula-search/', views.sumula_search_view, name='sumula-searchs-view'),
]
