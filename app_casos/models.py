from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import random  # Importação necessária para gerar um código único

class DisciplinaCasosModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
    

class RamoDireitoModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class TagCasoModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')



class CasoConcretoModel(models.Model):
    title = models.CharField(max_length=255, unique=True)
    disciplina = models.ForeignKey(DisciplinaCasosModel, on_delete=models.CASCADE)
    ramo_direito = models.ForeignKey(RamoDireitoModel, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)  # Corrigido para DateTimeField
    pergunta_caso = models.TextField()
    resposta_caso = models.TextField()
    fundamentacao = models.TextField(blank=True, null=True)
    meta_description = models.TextField(max_length=255)  # Corrigido para TextField
    keyword = models.CharField(blank=True)
    tags = models.ManyToManyField('TagCasoModel', blank=True)
    is_published = models.BooleanField(default=True)
    old_url = models.SlugField(blank=True, null=True)
    code = models.PositiveIntegerField(unique=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)  


    def generate_unique_code(self):
        code = random.randint(10000, 99999)
        while CasoConcretoModel.objects.filter(code=code).exists():
            code = random.randint(10000, 99999)
        return code

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.disciplina)  + ' | ' + str(self.ramo_direito) # Corrigido para disciplina
    


    def get_absolute_url(self):
        return reverse('app_casos:caso-single', kwargs={'slug': self.slug})

    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(CasoConcretoModel, self).save(*args, **kwargs)