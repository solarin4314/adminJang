from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class HijoSchema(models.Model):
    hijo_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hijo_title = models.CharField(max_length=200)
    hijo_text = models.TextField()
    hijo_created_date = models.DateTimeField(
            default=timezone.now)
    hijo_modify_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
