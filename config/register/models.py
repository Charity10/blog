from django.db import models

# Create your models here.
class UserDetails(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password1 = models.CharField(max_length=1000)
    ConfirmPasword = models.CharField(max_length=1000)

    def __str__(self):
        return self.firstname
