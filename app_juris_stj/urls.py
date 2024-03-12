from django.urls import path
from . views import STJjurisprudenciaView, STJjurisprudenciaSingularView
from . import views


app_name = 'app_juris_stj'

urlpatterns = [
    path('', STJjurisprudenciaView.as_view(), name='juris-stj-list'),
    path('juris-single/<int:pk>/', STJjurisprudenciaSingularView.as_view(), name='juris-stj-single'),
    path('stj-upload/', views.upload_jurisprudencia_view, name='juris-stj-upload'),
]
