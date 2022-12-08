"""Forms of the project."""
from django import forms
from django.core.validators import RegexValidator
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name','description', 'quantity']

    
    def clean(self):
        """Clean the data and generate messages for any errors."""
        super().clean()
    
    def save(self):
        super().save(commit=False)
        thing = Thing.objects.create(
            name = self.cleaned_data.get('name'),
            description = self.cleaned_data.get('descripquantity'),
            quantity = self.cleaned_data.get('quantity'),
        )
        return thing
