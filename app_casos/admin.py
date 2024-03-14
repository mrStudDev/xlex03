from django.contrib import admin

from .models import (
    CasoConcretoModel,
    DisciplinaCasosModel,
    RamoDireitoModel,
    TagCasoModel
    )

class CasosAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_created"]
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
