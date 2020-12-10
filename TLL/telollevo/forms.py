from django import forms
from .models import Envios

class EnviosForm(forms.ModelForm):
	class Meta:
		model = Envios
		fields = '__all__'