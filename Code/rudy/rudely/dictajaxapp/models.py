from django.db import models


class Dictionary(models.Model):
    word = models.CharField(max_length=20)
    definition = models.CharField(max_length=200)
    synonym = models.CharField(max_length=40)

    def __str__(self):
        return self.word + ' - ' + self.definition

