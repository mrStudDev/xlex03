# Generated by Django 5.0.3 on 2024-04-14 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_edu_social', '0002_articlessocialmodel_indexable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlessocialmodel',
            name='meta_description',
            field=models.TextField(max_length=160),
        ),
    ]
