from django.urls import path
from . import views
from . views import (
    DocumentListView,
    DocumentSingleView,
    RamoDocumentView,
    TagDocumentView,
    TipoDocumentView,
    CreateDocumentView,
    UpdateModeloView,
    DeleteModeloView,
    
    )

app_name = 'app_modelos'

urlpatterns = [
  path('', DocumentListView.as_view(), name='modelos-list'),
  path('modelo-single/<slug:slug>/', DocumentSingleView.as_view(), name='modelo-single'),
  path('ramo-direito-doc/<slug:ramo_slug>/', RamoDocumentView.as_view(), name='modelos-ramo-direito'),
  path('tipo-doc/<slug:tipo_slug>/', TipoDocumentView.as_view(), name='modelos-tipo-doc'),
  path('tags-docs/<slug:tag_slug>/', TagDocumentView.as_view(), name='modelos-tag-doc'),
  path('create-modelo/', CreateDocumentView.as_view(), name='modelo-create'),
  path('update-modelo/<slug:slug>/', UpdateModeloView.as_view(), name='modelo-update'),
  path('delete-modelo/<slug:slug>/', DeleteModeloView.as_view(), name='modelo-delete'),

]
