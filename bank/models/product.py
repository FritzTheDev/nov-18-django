from django.db.models import Model, CharField

product_type_choices = (
    ('crd', 'CREDIT'),
    ('chk', 'CHECKING'),
    ('svg', 'SAVINGS'),
)

class Product(Model):
    product_type = CharField(max_length=3, choices=product_type_choices)
    product_description = CharField(max_length=1000)

    def __str__(self):
        if self.product_type == 'crd':
            return 'Credit'
        if self.product_type == 'chk':
            return 'Checking'
        if self.product_type == 'crd':
            return 'Savings'
