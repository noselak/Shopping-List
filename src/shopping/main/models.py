from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=15)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    accepted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class ShoppingList(models.Model):
    name = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.CharField(max_length=15)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    @property
    def shopping_items(self):
        shopping_items = ShoppingItem.objects.filter(shopping_list=self)
        return shopping_items

    def __str__(self):
        return self.name


class ShoppingItem(models.Model):
    name = models.CharField(max_length=15, blank=True, null=True)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, null=True)
    shopping_list = models.ForeignKey('ShoppingList', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.item.name
