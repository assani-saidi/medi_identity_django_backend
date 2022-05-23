from django.db import models
from django.db.models.fields import CharField

from providers.models import Provider

# Create your models here.
class Employee(models.Model):
    name = models.CharField(null=False, max_length=100)
    surname = models.CharField(null=False, max_length=100)
    employment_number = models.CharField(null=False, max_length=10, unique=True)
    password = models.CharField(null=False, max_length=100)
    company = models.ForeignKey(to=Provider, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name