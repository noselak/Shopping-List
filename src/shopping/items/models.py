from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
