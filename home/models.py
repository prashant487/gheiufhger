from django.db import models


# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name


class contactinfo(models.Model):
    address = models.CharField(max_length=700)
    tole = models.CharField(max_length=400)
    contact_no = models.CharField(max_length=100)
    time = models.CharField(max_length=200)
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.address


class testm(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=700)
    comment = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name
