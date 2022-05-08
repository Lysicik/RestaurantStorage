from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import StockProduct, Contractor, Order, Employee, PackingList, Product, Giveaway, Account


class StockProductCreate (forms.ModelForm):
    class Meta:
        model = StockProduct
        fields = ['number_stoсk_product', 'product_stock', 'quantity_product', 'date_expire_product', 'product_order', 'product_contractor', 'product_employee', 'number_packing_list']
        error_messages = {
            'date_expire_product': {
                'invalid': "Неверный формат даты",
            },
        }

class ContractorCreate (forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['organization_name', 'phone', 'address']


class OrderCreate (forms.ModelForm):
    class Meta:
        model = Order
        fields = ['number_order', 'date_order', 'employee']
        error_messages = {
            'date_order': {
                'invalid': "Неверный формат даты",
            },
        }

class EmployeeCreate (forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['lastname', 'firstname', 'patronymic', 'birth_date', 'employee_address', 'position', 'salary']
        error_messages = {
            'birth_date': {
                'invalid': "Неверный формат даты",
            },
        }
        widgets = {
            'lastname': forms.TextInput(attrs={'pattern': '[а-яА-Я]+'})
        }

class PackingListCreate (forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ['number_list', 'contractor', 'product', 'date_expire', 'quantity', 'price', 'delivery_date', 'employee', 'order']
        error_messages = {
            'date_expire': {
                'invalid': "Неверный формат даты",
            },
            'delivery_date': {
                'invalid': "Неверный формат даты",
            },
        }



class ProductCreate (forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_type', 'product_name', 'shelf_line']


class GiveawayCreate (forms.ModelForm):
    class Meta:
        model = Giveaway
        fields = ['number_giveaway_list', 'product_away', 'quantity_product_away', 'date_away', 'reason', 'product_order_away', 'product_contractor_away', 'product_employee', 'number_packing_list_away']
        error_messages = {
            'date_away': {
                'invalid': "Неверный формат даты",
            },
        }

class SignIn (AuthenticationForm):
    class Meta:
        model = Account
        fields = ['username', 'password']