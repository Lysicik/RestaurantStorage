# Generated by Django 3.2.13 on 2022-04-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_employee_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packinglist',
            name='number_list',
            field=models.CharField(max_length=15, verbose_name='Номер товарной накладной'),
        ),
    ]