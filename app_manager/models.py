from django.db import models
from django.utils import timezone

class PageView(models.Model):
    page_name = models.CharField(max_length=255)
    view_count = models.IntegerField(default=0)
    last_accessed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.page_name} - Views: {self.view_count}"

class DailyPageView(models.Model):
    page = models.ForeignKey(PageView, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    view_count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.page.page_name} - {self.date} - Views: {self.view_count}"

    class Meta:
        unique_together = ('page', 'date')