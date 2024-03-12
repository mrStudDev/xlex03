from django.urls import path
from . import views
from . views import XlexHomeView, JurisprudenciasListView

app_name = 'app_home'

urlpatterns = [
    path('', XlexHomeView.as_view(), name='home-view'),
    path('contato/', views.contact_view, name='contact-us'),
    path('sobre-nos/', views.sobre_nos, name='sobre-nos'),
    path('jurisprudencias/', JurisprudenciasListView.as_view(), name='jurisprudencias-page-list'),
]