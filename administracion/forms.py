from django import forms

class ProyectosForm(forms.Form):
    foto=forms.URLField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    titulo_proyecto=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    descripcion_proyecto=forms.CharField(max_length=400, widget=forms.TextInput(attrs={'class':'form-control mb-3'}))