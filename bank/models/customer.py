from django.db.models import Model, OneToOneField, CharField, ForeignKey, CASCADE

class Customer(Model):
    base_user = OneToOneField('auth.User', on_delete=CASCADE, primary_key=True)
    first_name = CharField(max_length=15)
    last_name = CharField(max_length=20)