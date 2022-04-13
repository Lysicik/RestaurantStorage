from django.shortcuts import render
from app.models import Contractor


def index(request):
    contractors = Contractor.objects.get_table_data()

    return render(request, 'index.html', {
        "contractors": contractors,
    })
