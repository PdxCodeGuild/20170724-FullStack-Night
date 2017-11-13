from django.db import models

# Create your models here.


class Shortener(models.Model):
    url_text = models.CharField(max_length=500)
    code_text = models.CharField(max_length=20)

    def __str__(self):
        return self.url_text+self.code_text
