# Generated by Django 3.1.3 on 2020-11-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201128_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='description',
            field=models.TextField(verbose_name='Client say'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(verbose_name='About service'),
        ),
    ]
