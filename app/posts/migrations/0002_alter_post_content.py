# Generated by Django 4.0.5 on 2022-06-26 02:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=3000, verbose_name='Contenido'),
        ),
    ]
