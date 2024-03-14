from django.urls import path
from . import views

from . views import (
    CasoConcretoView,
    CasoSingularView,
    DisciplinaCasosView,
    RamoDireitocasoViews,
    TagCasosView,
    UpdateCasoView,
    CasoCreateView,
    CasoDeleteView,
)

app_name = 'app_casos'

urlpatterns = [
    path('', CasoConcretoView.as_view() ,name='casos-list'),
    path('caso/<slug:slug>/', CasoSingularView.as_view() ,name='caso-single'),
    path('disciplina/<slug:disciplina_caso_slug>/', DisciplinaCasosView.as_view(), name='casos-disciplinas'),
    path('ramo-direito/<slug:ramo_caso_slug>/', RamoDireitocasoViews.as_view(), name='casos-ramo-direito'),
    path('tags/<slug:tagCaso_slug>/', TagCasosView.as_view(), name='casos-tags'),
    path('caso-create/', CasoCreateView.as_view(), name='caso-create-post'),
    path('caso-update/<slug:slug>/', UpdateCasoView.as_view(), name='caso-update-post'),
    path('caso-delete/<slug:slug>/', CasoDeleteView.as_view(), name='caso-delete-post'),
]