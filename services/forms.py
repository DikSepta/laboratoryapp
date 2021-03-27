from django import forms
from services.models import Services

class AddService(forms.ModelForm):

    class Meta:
        model = Services 
        fields = ['service','description','price']
