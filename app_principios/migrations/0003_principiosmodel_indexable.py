# Generated by Django 5.0.3 on 2024-04-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principios', '0002_remove_principiosmodel_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='principiosmodel',
            name='indexable',
            field=models.BooleanField(default=True),
        ),
    ]
