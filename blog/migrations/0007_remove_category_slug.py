# Generated by Django 4.2.3 on 2023-08-09 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
