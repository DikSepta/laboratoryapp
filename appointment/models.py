from django.db import models
from django.conf import settings
from services.models import Services

STATUS_CHOICES = [
    ('WA', 'Waiting Approval'),
    ('A', 'Approved'),
    ('R', 'Rejected'),
    ('C', 'Canceled'),
    ('F', 'Finished')
]

# Create your models here.
class Appointment(models.Model):
    registration_id = models.PositiveIntegerField(unique=True)
    customer        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service         = models.ForeignKey(Services, on_delete=models.CASCADE)
    date            = models.DateField(verbose_name='date')
    status          = models.CharField(max_length=2, choices=STATUS_CHOICES, default='WA')

    def __str__(self):
        return str(self.registration_id)
    
    class Meta:
        ordering=["registration_id"]