from django.db import models

class Client(models.Model):
    name = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name

class Alert(models.Model):
    ip_address = models.GenericIPAddressField()
    ip_destination = models.GenericIPAddressField()
    packet_size = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Blocked', 'Blocked'),
        ('Suspicious', 'Suspicious'),
        ('Safe', 'Safe')
    ])
    client = models.ForeignKey(to=Client, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.ip_address} - {self.status} at {self.timestamp}"


# Create your models here.


