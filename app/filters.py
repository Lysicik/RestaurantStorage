import django_filters

from app.models import Contractor, Product


class ContractorFilter(django_filters.FilterSet):
    organization_name = django_filters.CharFilter(label='Название организации', lookup_expr='contains')

    class Meta:
        model = Contractor
        fields = ['organization_name']

class ProductFilter(django_filters.FilterSet):
    product_type = django_filters.CharFilter(label='Тип товара', lookup_expr='contains')
    product_name = django_filters.CharFilter(label='Название товара', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['product_type', 'product_name']
