from django import forms
from .models import Comentario, Pagar, Informar

class PagarForm(forms.ModelForm):

    class Meta:
        model = Pagar
        fields = ['nome', 'classe', 'valor', 'mes']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model= Comentario
        fields = ['opiniao']

class InformarForm(forms.ModelForm):

    class Meta:
        model = Informar
        fields = ['tema', 'info']
































 #       class PagarForm(forms.ModelForm):

  #  class Meta:
   #     model = Pagar
    #    fields = ['classe', 'nome','valor', 'mes', 'email']