from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class TribNameSumulaModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
class SiglaTribSumulaModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name  
    
class SumulaModel(models.Model):
    title = models.CharField(max_length=255)
    numero_sumula = models.CharField("Número da Súmula", max_length=9)
    sigla_tribunal = models.ForeignKey(SiglaTribSumulaModel, null=True, blank=True, on_delete=models.SET_NULL)
    nome_tribunal = models.ForeignKey(TribNameSumulaModel, null=True, blank=True, on_delete=models.SET_NULL)
    tema_juridico = models.CharField("Tema Jurídico", max_length=255)
    turma = models.CharField("Turma", max_length=255, default="Sem informação de Turma")
    enunciado = models.TextField()
    comentario = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    meta_description = models.CharField(max_length=150)
    keyword = models.CharField(max_length=150)
    is_published = models.BooleanField(default=True)
    old_url = models.SlugField(blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0) 

    def __str__(self):
        return f"Súmula {self.title} - {self.numero_sumula} - {self.sigla_tribunal} - {self.tema_juridico} - {self.enunciado}"

    def get_absolute_url(self):
        return reverse('app_sumulas:sumula-single', kwargs={'slug': self.slug})
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(SumulaModel, self).save(*args, **kwargs)