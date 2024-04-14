from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import random 


class RamoDireitoDocModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home-view')

class TipoDocumentModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home-view')

class TagDocumentsModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home-view')


class DocumentsModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    ramo_direito = models.ForeignKey(RamoDireitoDocModel, null=True, on_delete=models.CASCADE)
    tipo_doc = models.ForeignKey(TipoDocumentModel, null=True, on_delete=models.CASCADE)
    content_doc = models.TextField(blank=True, null=True)
    meta_description = models.TextField(max_length=170)
    keyword = models.CharField(max_length=255)
    tags = models.ManyToManyField('TagDocumentsModel', blank=True)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    code = models.PositiveIntegerField(unique=True, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    old_url = models.SlugField(blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    indexable = models.BooleanField(default=True)  # Novo campo para SEO

    def is_indexable(self):
        return self.indexable

    def generate_unique_code(self):
        code = random.randint(10000, 99999)
        while DocumentsModel.objects.filter(code=code).exists():
            code = random.randint(10000, 99999)
        return code

    def save(self, *args, **kwargs):
        try:
            if not self.code:
                self.code = self.generate_unique_code()
            if not self.slug:
                self.slug = slugify(self.title)
            super().save(*args, **kwargs)
        except Exception as e:
            print(f"Error saving document: {e}")
            # Handle or log the exception as needed


    def __str__(self):
        return str(self.title) + ' - ' + str(self.author)

    def get_absolute_url(self):
        return reverse('app_modelos:modelo-single', kwargs={'slug': self.slug})
    
    def update_views(self, *args, **kwargs):
        self.views = self.views + 1
        super(DocumentsModel, self).save(*args, **kwargs)