from django.forms import *
from Orion.models import models_comproba

class ComprobaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():
            #form.field.widget.attrs['class'] = 'form-control'
            #form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['codcomp'].widget.attrs['autofocus'] = True

    class Meta:
        model = models_comproba.Comproba
        fields = '__all__'
        labels = {
            'codcomp': 'Código',
            'descripcion': 'Descripción'
        }
        widgets = {
            'codcomp': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                }
            ),
            'descripcion': Textarea(
                attrs={
                    'placeholder': 'Ingrese un nombre',
                    #'rows': 3,
                    #'cols': 3
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
