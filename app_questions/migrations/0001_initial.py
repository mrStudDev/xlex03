# Generated by Django 5.0.3 on 2024-03-13 21:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BancaQuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaQuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RamoDireitoQuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecentAnswersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TagQuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='XlexQuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('question_ask', models.TextField(blank=True, null=True)),
                ('fundaments', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('meta_description', models.TextField(max_length=250)),
                ('keyword', models.CharField(max_length=250)),
                ('is_published', models.BooleanField(default=True)),
                ('old_url', models.SlugField(blank=True, null=True)),
                ('code', models.PositiveIntegerField(blank=True, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField(default=0)),
                ('banca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_questions.bancaquestionmodel')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_questions.disciplinaquestionmodel')),
                ('ramo_direito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_questions.ramodireitoquestionmodel')),
                ('tags', models.ManyToManyField(blank=True, to='app_questions.tagquestionmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AlternativasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternativa', to='app_questions.xlexquestionmodel')),
            ],
        ),
    ]