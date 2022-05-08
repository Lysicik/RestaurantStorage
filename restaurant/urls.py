"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contractors/', views.index),
    path('contractor/delete/<int:id>', views.delete_add_change, name='delete_add_change'),
    path('products/', views.index2),
    path('products/delete/<int:id>', views.delete_add_change2, name='delete_add_change2'),
    path('employees/', views.index3),
    path('employees/delete/<int:id>', views.delete_add_change3, name='delete_add_change3'),
    path('orders/', views.index4),
    path('orders/delete/<int:id>', views.delete_add_change4, name='delete_add_change4'),
    path('packinglists/', views.index5),
    path('packinglists/delete/<int:id>', views.delete_add_change5, name='delete_add_change5'),
    path('stockproducts/', views.index6),
    path('stockproducts/delete/<int:id>', views.delete_add_change6, name='delete_add_change6'),
    path('giveaways/', views.index7),
    path('giveaways/delete/<int:id>', views.delete_add_change7, name='delete_add_change7'),
    path('', views.auth),
    path('contractor/change/<int:id>', views.change, name='change'),
    path('contractor/add', views.add, name='add'),
    path('product/change/<int:id>', views.change2, name='change2'),
    path('product/add', views.add2, name='add2'),
    path('employee/change/<int:id>', views.change3, name='change3'),
    path('employee/add', views.add3, name='add3'),
    path('order/change/<int:id>', views.change4, name='change4'),
    path('order/add', views.add4, name='add4'),
    path('packinglist/change/<int:id>', views.change5, name='change5'),
    path('packinglist/add', views.add5, name='add5'),
    path('stockproduct/change/<int:id>', views.change6, name='change6'),
    path('stockproduct/add', views.add6, name='add6'),
    path('giveaway/change/<int:id>', views.change7, name='change7'),
    path('giveaway/add', views.add7, name='add7'),
    path('logout/', views.logoutButton, name='logout'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
