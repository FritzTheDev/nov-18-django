from django.contrib import admin

from .models.account import Account
from .models.customer import Customer
from .models.product import Product
from .models.branch import Branch

# Register your models here.

admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Branch)