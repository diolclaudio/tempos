from django import forms
from .models import Pagar, Comentario, Inscricoes

class InscricoesForm(forms.ModelForm):

    class Meta:
        model = Inscricoes
        fields = ['nome','sexo', 'idade', 'nascimento_dia',
                  'nascimento_mes', 'nascimento_ano', 'cell1', 'cell2', 'bi', 'emitido', 'distrito', 'bairro',
                  'celula', 'quarteirao', 'casa', 'doenca', 'qual_doenca', 'nome_pai','local_trabalho_pai', 'profissao_pai', 'cell_pai', 'nome_mae', 'local_trabalho_mae', 'profissao_mae', 'classe', 'curso', 'seccao', 'grupo', 'anterior', 'turma', 'aproveitamento']

class PagarForm(forms.ModelForm):

    class Meta:
        model = Pagar
        fields = ['classe', 'nome','valor', 'mes', 'email']

class ComentarioForm(forms.ModelForm):

    class Meta:
        model= Comentario
        fields = ['opiniao']