from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse

from items.models import Item


class ShoppingList(models.Model):
    name = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.CharField(max_length=15)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    archived = models.BooleanField(default=False)

    @property
    def shopping_items(self):
        shopping_items = ShoppingItem.objects.filter(shopping_list=self)
        return shopping_items

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lists:shopping_list_detail_view', args=[str(self.pk)])

    class Meta:
        ordering = ['-date']


class ShoppingItem(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             null=True, blank=True)
    shopping_list = models.ForeignKey('ShoppingList', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=ShoppingItem)
def default_name(sender, instance, *args, **kwargs):
    if not instance.name:
        instance.name = instance.item.name
