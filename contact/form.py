from django import forms
from django.core import validators


class FormContact(forms.Form):

    name = forms.CharField(
        label="Nombre",
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Nombre y Apellido'
            }            
        ),
        validators=[
            validators.MinLengthValidator(4, "El nombre es demaciado corto"),
            validators.RegexValidator(
                '^[a-zA-Zñ ]*$', 'el titulo esta mal formateado')
        ]
    )

    phone = forms.CharField(
        label="Telefono",
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Telefono'
            }            
        ),
        validators=[
            validators.MinLengthValidator(
                7, "El numero de telefono es muy corto"),
            validators.RegexValidator(
                '^[0-9]*$', 'El telefono esta mal formateado')
        ]
    )

    email = forms.EmailField(
        label="Correo",
        required=True,
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Correo'
            }            
        ),
        validators=[
            validators.EmailValidator()
        ]
    )

    messege= forms.CharField(
        label=None,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Mensaje'
            }            
        ),
        required=True,       
    )

    def __init__(self, *args, **kwargs):
        super(FormContact, self).__init__(*args, **kwargs)
        self.fields['name'].label = ""
        self.fields['phone'].label = ""
        self.fields['email'].label = ""
        self.fields['messege'].label = ""




    # class FormCotizacion(forms.Form):
    #     name =
        
    #     email = 
