from django.db.models import Model, OneToOneField, CharField, DateTimeField, ForeignKey, CASCADE

class Customer(Model):
    base_user = OneToOneField('auth.User', on_delete=CASCADE, primary_key=True)
    customer_since = DateTimeField(auto_now_add=True)
    first_name = CharField(max_length=15)
    last_name = CharField(max_length=20)
    