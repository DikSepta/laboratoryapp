from django.db import models

# Create your models here.
class Services(models.Model):
    service_id = models.PositiveIntegerField(unique=True)
    service = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0, verbose_name='price')

    def __str__(self):
        return self.service
