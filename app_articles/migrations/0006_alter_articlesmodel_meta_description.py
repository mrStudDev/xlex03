# Generated by Django 5.0.3 on 2024-04-14 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_articles', '0005_articlesmodel_indexable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesmodel',
            name='meta_description',
            field=models.TextField(max_length=150),
        ),
    ]