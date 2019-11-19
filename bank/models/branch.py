from django.db.models import Model, CharField
from uuid import uuid4

class Branch(Model):
    branch_uuid = CharField(default=uuid4(), max_length=36, primary_key=True)
    branch_address = CharField(max_length=100)
