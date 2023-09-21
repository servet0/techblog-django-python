# Generated by Django 4.2.5 on 2023-09-20 13:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0045_footer_copyright_name_footer_policy_footer_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle_main', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('home', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('contact', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('news', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('popular', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('follow', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('privacy', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('alsolike', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('page', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]