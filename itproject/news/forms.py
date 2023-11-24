from .models import Artiles
from django.forms import ModelForm, TextInput, Textarea


class ArtilesForm(ModelForm):

    class Meta:
        model = Artiles
        fields = ['anons', 'full_text']

        {
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'anons'

            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text'

            })
        }


