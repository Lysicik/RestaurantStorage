# Generated by Django 3.2.13 on 2022-04-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220421_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(verbose_name='Оклад'),
        ),
    ]
