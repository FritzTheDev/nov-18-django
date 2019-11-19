from django.db.models import Model, ForeignKey, CharField, DateTimeField, CASCADE

class Account(Model):
    owner = ForeignKey('bank.models.customer', on_delete=CASCADE, related_name='accounts')
    account_name = CharField(max_length=255)
    created_on = DateTimeField(auto_now_add=True)
    