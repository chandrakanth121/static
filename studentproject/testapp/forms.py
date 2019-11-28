from django import forms
from testapp.models import studentmodel

class studentform(forms.ModelForm):
    class Meta:
        Model=studentmodel
        fields='__all__'
