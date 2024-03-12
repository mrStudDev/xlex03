from django.urls import path
from . import views
from . views import (
    PrincipiosListView,
    PrincipiosSingleView,
    RamoDireitoListView,
)

app_name = 'app_principios'

urlpatterns = [
    path('', PrincipiosListView.as_view(), name='principios-list'),
    path('principio-single/<slug:slug>/', PrincipiosSingleView.as_view(), name='principio-single'),
    path('principio-ramos/<slug:ramo_slug>/', RamoDireitoListView.as_view(), name='principios-ramo-direito'),
]
