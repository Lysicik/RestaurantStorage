from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователи')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class ContractorManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-organization_name')


class Contractor(models.Model):
    organization_name = models.CharField(max_length=100, verbose_name="Наименование организации")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    address = models.CharField(max_length=100, verbose_name="Адрес поставщика")

    objects = ContractorManager()

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
