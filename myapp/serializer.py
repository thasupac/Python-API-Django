from rest_framework import serializers
from .models import *


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        # fields = ("__All__")
        fields = ("id", "tid", "name", "department", "machine","tel")