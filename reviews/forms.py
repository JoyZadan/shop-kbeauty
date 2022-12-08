from django import forms
from .models import Review
from products.models import Category
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    """ Create form based on Review model """

    class Meta:
        model = Review
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        """ Adds placeholders and classes """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'title',
            'content': 'content',
        }
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
