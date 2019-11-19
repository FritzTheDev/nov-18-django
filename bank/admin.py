from django.contrib import admin

from .models.account import Account
from .models.customer import Customer
from .models.product import Product
from .models.branch import Branch

# Register your models here.

admin.site.register(Product)
admin.site.register(Account)


class AccountInline(admin.TabularInline):
    model = Account

class CustomerInline(admin.TabularInline):
    model = Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        AccountInline,
    ]

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    inlines = [
        CustomerInline
    ]
