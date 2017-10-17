from django.db import models

class UrlReroute(models.Model):
    code = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
