# Generated by Django 3.0.3 on 2020-05-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_app', '0002_auto_20200518_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='plataforma',
            name='descricao',
            field=models.CharField(default='', max_length=256),
        ),
    ]
