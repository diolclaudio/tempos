from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from.models import Comentario, Pagar, Informar
from .forms import ComentarioForm, InformarForm
from .forms import PagarForm

def index(request):
    return render(request, 'pays/index.html')

#Cria um formulario do aluno para pagar a mensalidade
@login_required
def pagamentos(request):
   return render(request, 'pays/pagamentos.html',)

#Listas dos pagamentos
def oito(request):
    return render(request, 'pays/pagamentos/oito.html')

def nove(request):
    return render(request, 'pays/pagamentos/none.html')

def dez(request):
    return render(request, 'pays/pagamentos/dez.html')

    #decima primeira
def primeira(request):
    return render(request, 'pays/pagamentos/primeira.html')

    #decima segunda
def segunda(request):
    return render(request, 'pays/pagamentos/segunda.html')

#Turmas que devem pagar
def oitoa(request):
    pagar = Pagar.objects.filter(user=request.user)

    if request.method == 'POST':
        form = PagarForm(request.POST)

        if form.is_valid():
            pagar = form.save(commit=False)
            pagar.user = request.user
            pagar.save()
            messages.info(request, 'As informacoes do aluno estao salvas. Agora clique no pay para pagar a mensalidade')

            return redirect('/oitava_a/')
    else:
        form = PagarForm()
        return render(request, 'pays/pagamentos/turmas/oitoa.html', {'form': form, 'pagar':pagar})


#Da informacoes sobre a escola
def info(request):
    informar = Informar.objects.all()
    comentario = Comentario.objects.all().order_by('-data')
    return render(request, 'pays/info.html', {'comentario': comentario, 'informar':informar})

#Cria um formulario para o usuario comentar sobre o site
def comentario(request):
    if request.method == 'POST':

        form = ComentarioForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('/info/')

    else:
        form = ComentarioForm()
        return render(request, 'pays/comentario.html', {'form': form})

def listas(request):
    return render(request, 'pays/listas.html', )

def hor(request):
    return render(request, 'pays/hor.html')


























#Listas dos alunos
def oita(request):
    return render(request, 'pays/oita.html',)

def nona(request):
    return render(request, 'pays/nona.html')

def decima(request):
    return render(request, 'pays/decima.html')

def onze(request):
    return render(request, 'pays/onze.html')

def doze(request):
    return render(request, 'pays/doze.html')