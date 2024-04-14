from django.contrib import admin
from .models import HomeSite, TagSiteModel, ContactMessagesModel


class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'indexable', '__str__')  # Adiciona indexable e mantém __str__
    list_editable = ('indexable',)  # Permite que indexable seja editável diretamente na lista
    list_filter = ('indexable',)  # Adiciona indexable aos filtros
    search_fields = ('site_name',)
    prepopulated_fields = {"slug": ("site_name",)}

    class Meta:
        models = HomeSite
        
class TagSiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = TagSiteModel
    
    
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactMessagesModel
        
admin.site.register(HomeSite, SiteAdmin)
admin.site.register(TagSiteModel, TagSiteAdmin)
admin.site.register(ContactMessagesModel, ContactAdmin)