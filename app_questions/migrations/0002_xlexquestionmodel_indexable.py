# Generated by Django 5.0.3 on 2024-04-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xlexquestionmodel',
            name='indexable',
            field=models.BooleanField(default=True),
        ),
    ]
