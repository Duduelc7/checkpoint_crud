from django import forms
from .models import *




class EmpresaForm(forms.ModelForm):    
    class Meta:
        model = Empresas
        fields = "__all__"

