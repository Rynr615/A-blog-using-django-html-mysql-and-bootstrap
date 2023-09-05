# Generated by Django 4.2.3 on 2023-08-31 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kontak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=70)),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(choices=[('p', 'Pria'), ('w', 'Wanita')], max_length=50)),
                ('alamat', models.TextField()),
                ('agree', models.BooleanField()),
            ],
        ),
    ]
