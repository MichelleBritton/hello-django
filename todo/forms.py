from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # Tell the form which model it's going to be associated with
    # This inner class just gives our form some information about itself like which fields it should render, how it should display error messages etc
    class Meta:
        model = Item
        fields = ['name', 'done']
