from django.contrib import admin

from .models import (
    Expenses,
    Order,  # ,Codadoc ,Codadocuments,Codadocs
    Picture,
    Service,
    Payments,
)

# Register your models here.
admin.site.register(Picture)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Expenses)
# admin.site.register(Codadocs)
# admin.site.register(Codadoc)
admin.site.register(Payments)
