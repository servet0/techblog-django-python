# Generated by Django 4.2.5 on 2023-09-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_logo_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='default',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]