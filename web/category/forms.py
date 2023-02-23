from django import forms
from django.utils.translation import gettext_lazy as _

from . import models

class CategoryForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=models.Category.objects.filter(parent=None), required=False, widget=forms.Select(attrs={'class': 'form-control'}), label=_('Main Category'))

    class Meta:
        model = models.Category
        fields = ('name', 'parent', 'status')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }