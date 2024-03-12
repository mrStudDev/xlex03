from django.shortcuts import render
from django.utils import timezone
from .models import PageView, DailyPageView
from typing import Any
from django.db.models import Sum

from django.views.generic import (
    ListView,
    DateDetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class ManagerView(ListView):
    model = PageView
    template_name = 'templates_manager/manager_admin.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['page'] = PageView.objects.all()
        context['pages'] = PageView.objects.all().order_by('-view_count')
        context['total_views'] = PageView.objects.aggregate(total=Sum('view_count'))['total'] or 0

        context["hide_sidebar"] = True
        context['current_app'] = 'app_manager'

        daily_views = DailyPageView.objects.values('date').annotate(total=Sum('view_count')).order_by('-date')
        context['daily_views'] = daily_views
        total_views = PageView.objects.aggregate(total=Sum('view_count'))['total'] or 0
        context['total_views'] = total_views
        return context
    
def update_page_view(page_name):
    page_view, _ = PageView.objects.get_or_create(page_name=page_name)
    page_view.view_count += 1
    page_view.last_accessed = timezone.now()
    page_view.save()

    today = timezone.now().date()
    daily_view, created = DailyPageView.objects.get_or_create(page=page_view, date=today)
    if not created:
        daily_view.view_count += 1
        daily_view.save()