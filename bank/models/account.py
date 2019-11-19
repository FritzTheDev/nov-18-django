from django.db.models import Model, ForeignKey, CharField, DateTimeField, CASCADE

account_type_choices = (
    ('crd', 'CREDIT'),
    ('chk', 'CHECKING'),
    ('svg', 'SAVINGS'),
)

class Account(Model):
    owner = ForeignKey('bank.customer', on_delete=CASCADE, related_name='accounts')
    account_name = CharField(max_length=25)
    account_type = CharField(max_length=3, choices=account_type_choices)
    created_on = DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.owner.first_name}'s {self.account_name}"
