from django.db import models

# Create your models here.
class Client(models.Model):
    fullname = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    cognitive = models.IntegerField()
    social = models.IntegerField()
    emotional = models.IntegerField()
    spiritual = models.IntegerField()
    physical = models.IntegerField()

    def __str__(self):
        return self.fullname
