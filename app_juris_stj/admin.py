from django.contrib import admin

from .models import STJJurisprudenciaUpload, STJjurisprudenciaModel


class STJUploadAdmin(admin.ModelAdmin):
    list_display = ["__str__", "uploaded_at"]
    list_filter = ["uploaded_at"]
    search_fields = ["title"]


class STJJurisAdmin(admin.ModelAdmin):
    list_display = ["__str__", ""]
    list_filter = [""]
    search_fields = [""]


admin.site.register(STJJurisprudenciaUpload, STJUploadAdmin)
admin.site.register(STJjurisprudenciaModel, )


