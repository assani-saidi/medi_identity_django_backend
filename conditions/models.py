from django.db import models
from django.db.models.fields import DateField

# Create your models here.
class Condition(models.Model):
    illness = models.CharField(null=False, max_length=200)
    treatment = models.TextField(null=False)
    diagnosed = DateField(null=False, auto_now_add=True)

    def _str_(self):
        return self.illness[1, 10]