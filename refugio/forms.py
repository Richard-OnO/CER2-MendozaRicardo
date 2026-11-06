from django import forms
from .models import Mascota

#Formulario de Mascota para la gestión web
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'descripcion', 'sexo', 'edad_aproximada', 'imagen', 'especie']