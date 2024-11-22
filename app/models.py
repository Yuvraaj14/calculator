from django.db import models

class Calculation(models.Model):
    operation = models.CharField(max_length=50)
    operands = models.CharField(max_length=100)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)