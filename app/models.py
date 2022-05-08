from django.db import models
from django.contrib.auth.models import User



class ContractorManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-organization_name').reverse()


class Contractor(models.Model):
    organization_name = models.CharField(max_length=100, verbose_name="Наименование организации")
    phone = models.CharField(max_length=16, verbose_name="Номер телефона")
    address = models.CharField(max_length=100, verbose_name="Адрес поставщика")

    objects = ContractorManager()

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class ProductManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-product_type').reverse()


class Product(models.Model):
    product_type = models.CharField(max_length=100, verbose_name="Тип товара")
    product_name = models.CharField(max_length=100, verbose_name="Название товара")
    shelf_line = models.CharField(max_length=10, verbose_name="Срок годности")

    objects = ProductManager()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



class EmployeeManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-lastname').reverse()


class Employee(models.Model):
    lastname = models.CharField(max_length=100, verbose_name="Фамилия")
    firstname = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    birth_date = models.DateField(max_length=10, verbose_name="Дата рождения")
    employee_address = models.CharField(max_length=100, verbose_name="Адрес сотрудника")
    position = models.CharField(max_length=100, verbose_name="Должность")
    salary = models.IntegerField(verbose_name="Оклад")

    objects = EmployeeManager()

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class OrderManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-employee')


class Order(models.Model):
    number_order = models.CharField(max_length=15, unique=True, verbose_name="Код заказа")
    date_order = models.DateField(verbose_name="Дата заказа")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, max_length=100, verbose_name="Сотрудник")

    objects = OrderManager()

    def __str__(self):
        return self.number_order

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class PackingListManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-number_list')


class PackingList(models.Model):
    number_list = models.CharField(max_length=15, verbose_name="Номер товарной накладной")
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, max_length=100, verbose_name="Поставщик")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=100, verbose_name="Товар")
    date_expire = models.DateField(verbose_name="Дата окончания срока годности")
    quantity = models.IntegerField(verbose_name="Количество")
    price = models.IntegerField(verbose_name="Цена")
    delivery_date = models.DateField(verbose_name="Дата поставки")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, max_length=100, verbose_name="Сотрудник")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, max_length=100, verbose_name="Код заказа")

    objects = PackingListManager()

    def __str__(self):
        return self.number_list

    class Meta:
        verbose_name = 'Товарная накладная'
        verbose_name_plural = 'Товарные накладные'

class StockProductManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-number_stoсk_product')


class StockProduct(models.Model):
    number_stoсk_product = models.CharField(max_length=15, unique=True, verbose_name="Номер товара на складе")
    product_stock = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=100, verbose_name="Товар")
    quantity_product = models.IntegerField(verbose_name="Количество")
    date_expire_product = models.DateField(verbose_name="Дата окончания срока годности")
    product_order = models.ForeignKey(Order, on_delete=models.CASCADE, max_length=100, verbose_name="Код заказа")
    product_contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, max_length=100, verbose_name="Поставщик")
    product_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, max_length=100, verbose_name="Сотрудник")
    number_packing_list = models.ForeignKey(PackingList, on_delete=models.CASCADE, max_length=15, verbose_name="Номер товарной накладной")


    objects = StockProductManager()

    def __str__(self):
        return self.product_stock

    class Meta:
        verbose_name = 'Товар на складе'
        verbose_name_plural = 'Товары на складе'



class GiveawayManager(models.Manager):
    def get_table_data(self):
        return self.order_by('-number_giveaway_list')


class Giveaway(models.Model):
    number_giveaway_list = models.CharField(max_length=15, verbose_name="Номер накладной выдачи/списания")
    product_away = models.ForeignKey(Product, on_delete=models.CASCADE, max_length=100, verbose_name="Товар")
    quantity_product_away = models.IntegerField(verbose_name="Количество")
    date_away = models.DateField(verbose_name="Дата выдачи/списания")
    reason = models.CharField(max_length=250, verbose_name="Причина")
    product_order_away = models.ForeignKey(Order, on_delete=models.CASCADE, max_length=100, verbose_name="Код заказа")
    product_contractor_away = models.ForeignKey(Contractor, on_delete=models.CASCADE, max_length=100, verbose_name="Поставщик")
    product_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, max_length=100, verbose_name="Сотрудник")
    number_packing_list_away = models.ForeignKey(PackingList, on_delete=models.CASCADE, max_length=15, verbose_name="Номер товарной накладной")


    objects = GiveawayManager()

    def __str__(self):
        return self.product_away.product_name

    class Meta:
        verbose_name = 'Накладная выдачи/списания'
        verbose_name_plural = 'Накладные выдачи/списания'


class Account(User):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
