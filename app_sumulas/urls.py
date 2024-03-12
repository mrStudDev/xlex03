from django.urls import path
from . views import (
    SumulasListView,
    SumulaSingularView,
    CreateSumulaView,
    UpdateSumulaView,
    DeleteSumulaView,
    TribNameSumulaView,
    SiglaTribSumulasView
    )
from . import views

app_name = 'app_sumulas'

urlpatterns = [
    path('', SumulasListView.as_view(), name='sumulas-list'),
    path('sumula-singular/<slug:sumula_slug>/', SumulaSingularView.as_view(), name='sumula-single'),
    path('sumula-create/', CreateSumulaView.as_view(), name='sumula-create-post'),
    path('sumula-update/<slug:slug>/', UpdateSumulaView.as_view(), name='sumula-update-post'),
    path('sumula-deletete/<slug:slug>/', DeleteSumulaView.as_view(), name='sumula-delete-post'),
    path('sumulas-tribunais/<slug:tribNameSum_slug>/', TribNameSumulaView.as_view(), name='sumula-tribunais-list'),
    path('sumulas-siglas/<slug:siglaTrib_slug>/', TribNameSumulaView.as_view(), name='sumula-tribunais-list'),

]