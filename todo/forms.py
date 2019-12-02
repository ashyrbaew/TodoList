from django import forms
from .models import TodoList

class AddItemForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('item', 'cover')