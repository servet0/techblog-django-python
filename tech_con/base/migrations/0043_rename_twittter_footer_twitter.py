# Generated by Django 4.2.5 on 2023-09-18 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_footer_available_footer_date_footer_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer',
            old_name='twittter',
            new_name='twitter',
        ),
    ]
