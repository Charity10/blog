from django.db import models

# Create your models here.
class UserLogin(models.Model):
    username = models.CharField(max_length=200)
    password1 = models.CharField(max_length=1000)

    def __str__():
        return self.username