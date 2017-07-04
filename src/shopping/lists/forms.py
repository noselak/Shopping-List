from django import forms

from .models import ShoppingList


class ListCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ListCreateForm, self).__init__(*args, **kwargs)
        for field in self.Meta.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': self.fields[field].label
            })
            if field == 'date':
                self.fields[field].widget.attrs.update(
                    {
                        'class': 'form-control datepicker',
                        'placeholder': self.fields[field].label
                    }
                )

    class Meta:
        model = ShoppingList
        fields = ['name', 'shop', 'date']
        labels = {
            'name': 'List Name',
            'shop': 'Shop',
            'date': 'Date',
        }
