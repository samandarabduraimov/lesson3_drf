from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    phone  = models.IntegerField()

    class Meta:
        db_table = 'drfapp'

    def __str__(self):
        return self.username