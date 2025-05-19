from django.db import models
import uuid

class Maintenance(models.Model):   #จะส่ง maintenance ไปที่ admin.py
    tid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    machine = models.CharField(max_length=255)
    problem = models.TextField()
    tel = models.CharField(max_length=12)

    def __str__(self):
        return self.name
