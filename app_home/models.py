from django.db import models
from django.utils.text import slugify

class TagSiteModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    

class HomeSite(models.Model):
    site_name = models.CharField(max_length=255)
    site_description = models.TextField()  # Alterado para TextField
    meta_title = models.CharField(max_length=255, default="Default Meta Title")
    meta_description = models.TextField(max_length=320)  # Capacidade aumentada
    founder = models.CharField(max_length=100)
    keyword = models.CharField(max_length=255)
    tags = models.ManyToManyField('TagSiteModel', blank=True)
    date_created = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    old_url = models.SlugField(blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    views = models.IntegerField(default=0)
    indexable = models.BooleanField(default=True)  # Novo campo para SEO

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.site_name)
        super(HomeSite, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.site_name} | {self.founder} | {self.views}"
    
    def update_views(self):
        self.views += 1
        self.save()


class ContactMessagesModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.subject