from django import forms


class ContactForm(forms.Form):
    nomape = forms.CharField(
        label='Nombres y Apellidos',
    )

    numtel = forms.CharField(
        label='Número de Teléfono',
    )

    email = forms.EmailField(
        label='Correo Electrónico',
    )

    asunto = forms.CharField(
        label='Asunto',
    )

    mensaje = forms.CharField(
        label='Mensaje',
        widget=forms.Textarea,
    )