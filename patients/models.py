from django.db import models
# from drf_extra_fields.fields import Base64ImageField

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    id_number = models.CharField(max_length=100, null=False, unique=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=500, blank=True)
    password = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=False, unique=True)
    image = models.ImageField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def _str_(self):
        return self.name



    