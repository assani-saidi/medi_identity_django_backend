from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField(null=False, max_length=100)
    address = models.CharField(null=False, max_length=500)
    contact = models.CharField(null=True, max_length=100)

    def _str_(self):
        return self.name
