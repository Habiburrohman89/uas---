# Generated by Django 4.1.3 on 2022-12-28 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabungan', '0002_remove_gadai_nominal_gadai_biaya_administrasi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadai',
            name='Bunga_Per_Th',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
