from django.db import models

# Create your models here.

class RescueReport(models.Model):
    location = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='rescues/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # E.g., Pending, In Progress, Resolved

    def __str__(self):
        return f"Rescue Report at {self.location} ({self.status})"



