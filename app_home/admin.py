from django.contrib import admin
from .models import HomeSite, TagSiteModel, ContactMessagesModel


class SiteAdmin(admin.ModelAdmin):
    list_display = ["__str__", "site_name"]
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
admin.site.register(TagSiteModel)
admin.site.register(ContactMessagesModel, ContactAdmin)