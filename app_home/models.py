from django.db import models


class TagSiteModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    

class HomeSite(models.Model):
    site_name = models.CharField(max_length=255)
    site_description = models.CharField(max_length=500)
    founder = models.CharField(max_length=100)
    meta_description = models.TextField(max_length=255)
    keyword = models.CharField(max_length=255)
    tags = models.ManyToManyField('TagSiteModel', blank=True)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    is_published = models.BooleanField(default=True)
    old_url = models.SlugField(blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.site_name} | {self.founder} | {self.views}"
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(HomeSite, self).save(*args, **kwargs)


class ContactMessagesModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.subject