from django.db import models
from django.conf import settings
# Create your models here.

class Ticket(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open', 'Open',
        IN_PROGRESS = 'in_progress', 'In Progress',
        CLOSED = 'closed', 'Closed',  
    title = models.CharField(
        max_length=100
    )
    description = models.TextField(
        max_length=3000,
    )
    status = models.CharField(
        max_length=12,
        choices=Status.choices,
        default=Status.OPEN,
    )
    created_at = models.DateTimeField(auto_now_add=True)
