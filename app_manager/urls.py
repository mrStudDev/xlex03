from django.urls import path
from . import views
from . views import (
    ManagerView
)

app_name = 'app_manager'

urlpatterns = [
    path('', ManagerView.as_view(), name='manager-admin-dash'),
    
]
