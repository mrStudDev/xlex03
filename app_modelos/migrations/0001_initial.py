# Generated by Django 5.0.3 on 2024-03-14 00:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RamoDireitoDocModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TagDocumentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, null=True, upload_to='modelos_docs/')),
                ('content', models.TextField(blank=True, null=True)),
                ('meta_description', models.TextField(max_length=170)),
                ('keyword', models.CharField(max_length=255)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('code', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('is_published', models.BooleanField(default=True)),
                ('old_url', models.SlugField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ramo_direito', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='app_modelos.ramodireitodocmodel')),
                ('tags', models.ManyToManyField(blank=True, to='app_modelos.tagdocumentsmodel')),
                ('tipo_doc', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='app_modelos.tipodocumentmodel')),
            ],
        ),
    ]
