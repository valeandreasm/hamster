from django import forms

class FormUsuario(forms.Form):
    nombre = forms.CharField(label = 'nombre', max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo = forms.CharField(label = 'correo', max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))