from django.db import models
import uuid

# Create your models here.
class List(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    due_date = models.DateField()
    is_done = models.BooleanField(default=False)
