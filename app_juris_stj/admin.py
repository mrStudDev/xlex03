from django.contrib import admin

from .models import STJJurisprudenciaUpload, STJjurisprudenciaModel


class STJUploadAdmin(admin.ModelAdmin):
    list_display = ["__str__", "uploaded_at"]
    list_filter = ["uploaded_at"]
    search_fields = ["title"]


class STJJurisAdmin(admin.ModelAdmin):
    list_display = ('numeroProcesso', 'indexable', '__str__')  # Adiciona indexable e mantém __str__
    list_editable = ('indexable',)  # Permite que indexable seja editável diretamente na lista
    list_filter = ('indexable',)  # Adiciona indexable aos filtros    list_display = ["__str__", ""]
    list_filter = ["numeroProcesso"]
    search_fields = [""]


admin.site.register(STJJurisprudenciaUpload, STJUploadAdmin)
admin.site.register(STJjurisprudenciaModel, STJJurisAdmin)


