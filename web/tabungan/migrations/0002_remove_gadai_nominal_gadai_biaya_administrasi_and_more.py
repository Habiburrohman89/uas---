# Generated by Django 4.1.3 on 2022-12-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabungan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gadai',
            name='Nominal',
        ),
        migrations.AddField(
            model_name='gadai',
            name='Biaya_administrasi',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='gadai',
            name='Bunga_Per_Th',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='gadai',
            name='Jumlah_Pinjaman',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]