from django.db import models
from . validators import validate_rut, validate_dose

# Create your models here.
class Drug(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vaccination(models.Model):
    rut = models.TextField(validators=[validate_rut])
    dose = models.DecimalField(validators=[validate_dose], max_digits=3, decimal_places=2)
    date = models.DateField()
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='drugs')

    def __str__(self):
        return f'{self.rut} - {self.date}'
