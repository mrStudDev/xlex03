from django.contrib import admin
from .models import SumulaModel, TribNameSumulaModel, SiglaTribSumulaModel


class SumulaAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_created"]
    list_filter = ["date_created"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = SumulaModel
        
class TribNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = TribNameSumulaModel
        
class SiglaTribAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = SiglaTribSumulaModel

admin.site.register(SumulaModel, SumulaAdmin)
admin.site.register(TribNameSumulaModel, TribNameAdmin)
admin.site.register(SiglaTribSumulaModel, SiglaTribAdmin)