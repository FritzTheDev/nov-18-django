from django.db.models import Model, CharField

product_type_choices = (
    ('crd', 'CREDIT'),
    ('chk', 'CHECKING'),
    ('svg', 'SAVINGS'),
)

class Product(Model):
    product_type = CharField(max_length=3, choices=product_type_choices)