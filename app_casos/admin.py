from django.contrib import admin

from .models import (
    CasoConcretoModel,
    DisciplinaCasosModel,
    RamoDireitoModel,
    TagCasoModel
    )

class CasosAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'indexable', '__str__')  # Adiciona indexable e mantém __str__
    list_editable = ('indexable',)  # Permite que indexable seja editável diretamente na lista
    list_filter = ('indexable',)  # Adiciona indexable aos filtros
    list_filter = ["date_created"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = CasoConcretoModel

class DisciplinaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = DisciplinaCasosModel

class RamoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = RamoDireitoModel

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 

    class Meta:
        model = TagCasoModel

admin.site.register(CasoConcretoModel, CasosAdmin)
admin.site.register(DisciplinaCasosModel, DisciplinaAdmin)
admin.site.register(RamoDireitoModel, RamoAdmin)
admin.site.register(TagCasoModel, TagAdmin)
