# Generated by Django 5.0.3 on 2024-03-14 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_casos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casoconcretomodel',
            name='keyword',
            field=models.CharField(blank=True),
        ),
    ]