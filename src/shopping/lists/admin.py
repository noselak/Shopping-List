from django.contrib import admin

from .models import ShoppingList, ShoppingItem


class ShoppingItemInline(admin.TabularInline):
    model = ShoppingItem


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    inlines = [ShoppingItemInline]
    
    class Meta:
        model = ShoppingList


admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ShoppingItem)