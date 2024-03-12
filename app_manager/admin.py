from django.contrib import admin
from .models import PageView
# Register your models here.

class PageViewAdmin(admin.ModelAdmin):
    list_display = ["__str__", "page_name"]
    
    class Meta:
        model = PageView

admin.site.register(PageView, PageViewAdmin)