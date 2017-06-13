from django.contrib import admin

from .models import ShoppingList, ShoppingItem, Item, Category


class ShoppingItemInline(admin.TabularInline):
    model = ShoppingItem


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    inlines = [ShoppingItemInline]
    
    class Meta:
        model = ShoppingList


admin.site.register(Item)
admin.site.register(Category)
admin.site.register(ShoppingList, ShoppingListAdmin)
