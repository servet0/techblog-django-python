# Generated by Django 4.2.5 on 2023-09-14 10:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_header_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
