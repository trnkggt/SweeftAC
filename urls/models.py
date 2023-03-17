from django.db import models
# Create your models here.

class Url(models.Model):
    longurl = models.URLField(max_length=250)
    shorturl = models.URLField()
    is_premium = models.BooleanField(default=False)
    date_created = models.DateField(auto_now=True)

