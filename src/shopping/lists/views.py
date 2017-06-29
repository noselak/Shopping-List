from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from items.models import Item

from .models import ShoppingList, ShoppingItem
from .forms import ListCreateForm


class ShoppingListsView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'redirect_to'

    template_name = 'lists/shopping_lists.html'
    context_object_name = 'shopping_lists'

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


class ShoppingListDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'
    redirect_field_name = 'redirect_to'

    template_name = 'lists/shopping_list_detail.html'
    context_object_name = 'shopping_list'

    def get_queryset(self):
        return ShoppingList.objects.filter(user=self.request.user)


class ShoppingListDeleteView(View):
    @method_decorator(login_required(login_url='users:login_view'))
    def post(self, request, pk):
        shopping_list = ShoppingList.objects.get(pk=pk)
        if shopping_list.user == self.request.user:
            shopping_list.delete()
        return redirect('lists:shopping_lists_view')


class MarkShoppingItemView(View):
    @method_decorator(login_required(login_url='users:login_view'))
    def post(self, request):
        item_pk = int(request.POST.get('pk'))
        shopping_item = ShoppingItem.objects.get(pk=item_pk)

        if shopping_item.shopping_list.user == request.user:
            if shopping_item.bought is False:
                shopping_item.bought = True
            else:
                shopping_item.bought = False
            shopping_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddShoppingListView(View):
    @method_decorator(login_required(login_url='users:login_view'))
    def get(self, request):
        list_create_form = ListCreateForm(None)
        template = 'lists/add_shopping_list.html'
        context = {
            'list_create_form': list_create_form,
        }
        return render(request, template, context)

    @method_decorator(login_required(login_url='users:login_view'))
    def post(self, request):
        list_create_form = ListCreateForm(request.POST)

        if list_create_form.is_valid():
            new_list = list_create_form.save(commit=False)
            new_list.user = request.user
            new_list.save()

            return redirect('lists:shopping_list_detail_view', pk=new_list.pk)

        template = 'lists/add_shopping_list.html'
        context = {
            'list_create_form': list_create_form,
        }
        return render(request, template, context)


class AddItemsToListView(View):
    @method_decorator(login_required(login_url='users:login_view'))
    def get(self, request, pk):
        shopping_list = ShoppingList.objects.get(pk=pk)
        template = 'lists/add_items_to_list.html'
        context = {
            'shopping_list': shopping_list,
        }
        return render(request, template, context)

    @method_decorator(login_required(login_url='users:login_view'))
    def post(self, request, pk):
        shopping_list = ShoppingList.objects.get(pk=pk)
        item_pk = request.POST.get('item-pk')
        item = None
        
        try:
            item = Item.objects.get(pk=item_pk)
        except:
            pass
        
        if item:
            obj, created = ShoppingItem.objects.get_or_create(
                    item=item, shopping_list=shopping_list)
            
            if not created:
                obj.quantity = obj.quantity + 1
                obj.save()

        else:
            obj = ShoppingItem.objects.create(
                    shopping_list=shopping_list)

        return redirect('lists:shopping_list_detail_view', pk=shopping_list.pk)
