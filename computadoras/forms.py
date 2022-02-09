from django.forms import ModelForm, TextInput
from computadoras.models import *

class CompuForm(ModelForm):
    class Meta:
        model = Computadora
        fields = '__all__'

class TecladoForm(ModelForm):
    class Meta:
        model = Teclado
        fields = '__all__'

class MonitorForm(ModelForm):
    class Meta:
        model = Monitor
        fields = '__all__'
        widgets = {
            'width': TextInput(attrs={'type': 'number'})
        }

class MouseForm(ModelForm):
    class Meta:
        model = Mouse
        fields = '__all__'
