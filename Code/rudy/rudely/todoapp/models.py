from django.db import models


class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    date_entered = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)    #

    def __str__(self):
        return self.todo_text

    def completed(self):
        return self.date_entered is not None
