from django.contrib import admin
from .models import (
    DocumentsModel,
    RamoDireitoDocModel,
    TipoDocumentModel,
    TagDocumentsModel,
)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_created"]
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