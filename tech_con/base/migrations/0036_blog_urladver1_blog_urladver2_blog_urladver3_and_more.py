# Generated by Django 4.2.5 on 2023-09-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_rename_urlheaderurl_mainadversiment_urlheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='urladver1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='urladver2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='urladver3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='urladver4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='urladver1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='urladver2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='urladver3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='urladver4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header2',
            name='urladver1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header2',
            name='urladver2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header2',
            name='urladver3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header2',
            name='urladver4',
            field=models.URLField(blank=True, null=True),
        ),
    ]
