from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    contact = models.IntegerField()
    address = models.TextField()
    captcha = models.CharField(max_length=50)

    def __str__(self):
        return self.name
