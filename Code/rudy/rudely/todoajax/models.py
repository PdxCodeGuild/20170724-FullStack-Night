from django.db import models


class TodoajaxItem(models.Model):
    todo_text = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.todo_text

