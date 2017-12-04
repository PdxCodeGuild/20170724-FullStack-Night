from django.db import models

# Create your models here.

class DictAjaxEntry:
    word = models.CharField(max_length=200)
    definition = models.CharField(max_length=500)

    def __str__(self):
        return self.word

