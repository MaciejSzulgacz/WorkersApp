from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=24)
    surname = models.CharField(max_length=24)
    age = models.SmallIntegerField()
    profession = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='./images/')

    def __str__(self):
        return f"{self.name} {self.surname}"
