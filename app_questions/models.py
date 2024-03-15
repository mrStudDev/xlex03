from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models import Count
import random
from django.core.exceptions import ValidationError


class RecentAnswersModel(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class BancaQuestionModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class DisciplinaQuestionModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class RamoDireitoQuestionModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class TagQuestionModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class XlexQuestionModel(models.Model):
    title = models.CharField(max_length=255)
    banca = models.ForeignKey(BancaQuestionModel, on_delete=models.CASCADE)  
    disciplina = models.ForeignKey(DisciplinaQuestionModel, on_delete=models.CASCADE)
    ramo_direito = models.ForeignKey(RamoDireitoQuestionModel, on_delete=models.CASCADE)
    question_ask = models.TextField(blank=True, null=True)
    fundaments = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    tags = models.ManyToManyField('TagQuestionModel', blank=True)
    meta_description = models.TextField(max_length=250)
    keyword = models.CharField(max_length=250)
    is_published = models.BooleanField(default=True)
    old_url = models.SlugField(blank=True, null=True)
    code = models.PositiveIntegerField(unique=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0) 

    def clean(self):
        # Validação para garantir que o título não esteja vazio
        if self.title and self.title.strip() == '':
            raise ValidationError({'title': "O título não pode ser vazio."})

    def generate_unique_code(self):
        code = random.randint(100000, 999999)
        while XlexQuestionModel.objects.filter(code=code).exists():
            code = random.randint(100000, 999999)
        return code

    def save(self, *args, **kwargs):
        self.clean()

        if not self.slug:
            self.slug = slugify(self.title)
            if XlexQuestionModel.objects.filter(slug=self.slug).exists():
                raise ValidationError(f"O slug gerado a partir do título '{self.title}' já existe. Por favor, escolha um título diferente.")

        if not self.code:
            self.code = self.generate_unique_code()

        super(XlexQuestionModel, self).save(*args, **kwargs)
    

    def get_absolute_url(self):
        return reverse('app_questions:question-single', kwargs={'id': self.id, 'slug': self.slug})
    
    
    def update_views(self, *args, **kwargs):
         self.views = self.views + 1
         super(XlexQuestionModel, self).save(*args, **kwargs)


class AlternativasModel(models.Model):
    question = models.ForeignKey(XlexQuestionModel, on_delete=models.CASCADE, related_name='alternativa')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

