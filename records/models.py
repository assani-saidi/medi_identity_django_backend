from django.db import models
from django.db.models.fields import CharField
from conditions.models import Condition
from patients.models import Patient
from providers.models import Provider

# Create your models here.
class Record(models.Model):
    patient = models.ForeignKey(to=Patient, null=True, on_delete=models.SET_NULL)
    treatment = models.TextField(null=True)
    # dieses = models.ForeignKey(to=Condition, null=True, on_delete=models.SET_NULL)
    dieses = models.CharField(null=False, max_length=400)
    authorised_by = models.ForeignKey(to=Provider, null = True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.patient
