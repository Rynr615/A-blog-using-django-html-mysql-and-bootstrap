# Generated by Django 4.2.3 on 2023-08-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_artikel_penulis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
