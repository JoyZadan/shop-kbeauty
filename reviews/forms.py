from django import forms
from .models import Review
from products.models import Category, Product
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
            'title': 'Review Title',
            'content': 'Review Content',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['title'].widget.attrs['aria-label'] = 'Review Title'
        self.fields['content'].widget.attrs['aria-label'] = 'Review Content'

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False
