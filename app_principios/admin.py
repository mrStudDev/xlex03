from django.contrib import admin

from .models import (
    PrincipiosModel,
    RamoDireitoModel
)

class PrincipioAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'indexable', '__str__')  # Adiciona indexable e mantém __str__
    list_editable = ('indexable',)  # Permite que indexable seja editável diretamente na lista
    list_filter = ('indexable',)  # Adiciona indexable aos filtros
    list_filter = ["date_created"]
    search_fields = ["principio_name"]
    prepopulated_fields = {"slug": ("principio_name",)}
    
    class Meta:
        model = PrincipiosModel

class RamoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = RamoDireitoModel

admin.site.register(PrincipiosModel, PrincipioAdmin)
admin.site.register(RamoDireitoModel, RamoAdmin)