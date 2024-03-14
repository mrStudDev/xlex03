from django.contrib import admin

from .models import (
    CategoryArticlesModel,
    TagArticlesModel,
    ArticlesModel,
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date_created"]
    list_filter = ["date_created"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    
    class Meta:
        model = ArticlesModel

       
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = CategoryArticlesModel

                                            
class TagArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    

admin.site.register(ArticlesModel, ArticleAdmin)
admin.site.register(CategoryArticlesModel, CategoryAdmin)
admin.site.register(TagArticlesModel, TagArticleAdmin)
