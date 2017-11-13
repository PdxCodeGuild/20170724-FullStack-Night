from django.db import models


class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_color = models.CharField(max_length=50)
    contact_fruit = models.CharField(max_length=50)

    def __str__(self):
        return self.contact_name
