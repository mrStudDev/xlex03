from django.contrib import admin

from .models import (
    ArticlesSocialModel,
    CategorySocialModel,
    TagSocialModel
    )


class ArticleSocialAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_created"]
    list_filter = ["date_created"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    
    class Meta:
        model = ArticlesSocialModel

       
class CategorySocialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = CategorySocialModel

                                            
class TagArticleSocialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = TagSocialModel
    

admin.site.register(ArticlesSocialModel, ArticleSocialAdmin)
admin.site.register(CategorySocialModel, CategorySocialAdmin)
admin.site.register(TagSocialModel, TagArticleSocialAdmin)
