# Generated by Django 4.2.5 on 2023-09-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_rename_twittter_footer_twitter'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='youtube',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
