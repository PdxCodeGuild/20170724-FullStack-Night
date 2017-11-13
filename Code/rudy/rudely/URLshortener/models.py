from django.db import models

class Shortener(models.Model):
    original_url = models.CharField(max_length=100)
    code = models.CharField(max_length=20)



    def __str__(self):
        return self.original_url + ' ' + self.code



