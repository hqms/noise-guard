from django.db import models

class Alert(models.Model):
    ip_address = models.GenericIPAddressField()
    packet_size = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Blocked', 'Blocked'),
        ('Suspicious', 'Suspicious'),
        ('Safe', 'Safe')
    ])

    def __str__(self):
        return f"{self.ip_address} - {self.status} at {self.timestamp}"


# Create your models here.
