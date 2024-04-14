from django.contrib import admin
from .models import (
    DocumentsModel,
    RamoDireitoDocModel,
    TipoDocumentModel,
    TagDocumentsModel,
)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'indexable', '__str__')  # Adiciona indexable e mantém __str__
    list_editable = ('indexable',)  # Permite que indexable seja editável diretamente na lista
    list_filter = ('indexable',)  # Adiciona indexable aos filtros
    list_filter = ["date_created"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = DocumentsModel

class RamoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = RamoDireitoDocModel

class TipoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = TipoDocumentModel
        
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = TagDocumentsModel

admin.site.register(DocumentsModel, ModeloAdmin)
admin.site.register(TipoDocumentModel, TipoAdmin)
admin.site.register(RamoDireitoDocModel, RamoAdmin)
admin.site.register(TagDocumentsModel, TagAdmin)