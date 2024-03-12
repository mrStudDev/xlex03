from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.urls import reverse


class STJJurisprudenciaUpload(models.Model):
    title = models.CharField(max_length=150)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/stj_juris_files/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.description} em {self.uploaded_at.strftime('%Y-%m-%d %H:%M')} {self.title}"


class STJjurisprudenciaModel(models.Model):
    id_herdadoSTJ = models.CharField(max_length=500)
    numeroProcesso = models.CharField(max_length=500)
    numeroRegistro = models.CharField(max_length=500)
    siglaClasse = models.CharField(max_length=1000)
    descricaoClasse = models.CharField(max_length=1000)
    nomeOrgaoJulgador = models.CharField(max_length=1000)
    ministroRelator = models.CharField(max_length=1000)
    dataPublicacao = models.CharField(max_length=500)
    data_formatada = models.DateField(null=True, blank=True)    
    ementa = models.TextField()
    tipoDeDecisao = models.CharField(max_length=1000, null=True)
    dataDecisao = models.CharField(max_length=1000)
    decisao = models.TextField(null=True)
    jurisprudenciaCitada = models.TextField(null=True, default="Campo s/ dados")
    notas = models.CharField(max_length=1000, null=True, default="Campo s/ dados")
    informacoesComplementares = models.TextField(null=True, default="Campo s/ dados")
    termosAuxiliares = models.TextField(null=True, default="Campo s/ dados")
    teseJuridica = models.TextField(null=True, default="Campo s/ dados")
    tema = models.CharField(max_length=1000, null=True, default="Campo s/ dados")
    referenciasLegislativas = models.TextField(null=True, default="Campo s/ dados")
    acordaosSimilares = models.TextField(null=True, blank=True, default="Campo s/ dados")
    meta_description = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=255)
    keyword = models.CharField(max_length=200, blank=True, null=True, default="Campo s/ Key") 
    slug = models.SlugField(max_length=255, blank=True)
    views = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.numeroProcesso} | {self.ementa} | {self.data_formatada} | {self.title} | {self.views}"

    def get_absolute_url(self):
        return reverse('app_juris_stj:juris-stj-single', args=[str(self.id)])
    
    def update_views(self, *args, **kwargs):
        self.views = self.views + 1
        super(STJjurisprudenciaModel, self).save(*args, **kwargs)