from django.urls import path
from . import views
from . views import (
    PrincipiosListView,
    PrincipiosSingleView,
    RamoDireitoListView,
    PrincipioCreateView,
    UpdatePrincipioView,
    DeletePrincipioView
)

app_name = 'app_principios'

urlpatterns = [
    path('', PrincipiosListView.as_view(), name='principios-list'),
    path('principio-single/<slug:slug>/', PrincipiosSingleView.as_view(), name='principio-single'),
    path('principio-ramos/<slug:ramo_slug>/', RamoDireitoListView.as_view(), name='principios-ramo-direito'),
    path('principio-create/', PrincipioCreateView.as_view(), name='principios-create'),
    path('principio-update/<slug:slug>/', UpdatePrincipioView.as_view(), name='principio-update'),
    path('principio-delete/<slug:slug>/', DeletePrincipioView.as_view(), name='principio-delete'),
]
