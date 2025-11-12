from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        #fields = ["ip_address","packet_size", "client_id", "status"]
        fields = "__all__"