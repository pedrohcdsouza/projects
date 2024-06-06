from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=65)
    description = models.CharField(max_length=200)
    slug = models.SlugField()
    is_activated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

