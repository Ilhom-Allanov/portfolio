from django.db import models

class Portfolio(models.Model):
    image = models.ImageField()
    title = models.CharField()
    link = models.CharField()

    def __str__(self):
        return self.title
class Portfolio2(models.Model):
    image = models.ImageField()
    title = models.CharField()
    job = models.CharField()

    def __str__(self):
        return self.title
class Portfolio3(models.Model):
    title = models.CharField()
    message = models.CharField()

    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField()
    email = models.CharField()
    phone = models.CharField()
    message = models.CharField()

    def __str__(self):
        return self.name
