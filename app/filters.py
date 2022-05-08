import django_filters

from app.models import Contractor


class ContractorFilter(django_filters.FilterSet):
    class Meta:
        model = Contractor
        fields = {
            'organization_name': ['icontains']
        }
