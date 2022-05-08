from django.contrib import admin
from app import models

admin.site.register(models.Account)
admin.site.register(models.Contractor)
admin.site.register(models.Product)
admin.site.register(models.Employee)
admin.site.register(models.Order)
admin.site.register(models.PackingList)
admin.site.register(models.StockProduct)
admin.site.register(models.Giveaway)
