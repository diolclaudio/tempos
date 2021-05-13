from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import User
# Create your models here.

class Pagar(models.Model):
    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING)
    nome = models.CharField('Nome do aluno', max_length=50, choices=[('Diol Claudio', 'Diol Claudio'), ('joao fereira', 'joao fereira'), ('Loidmar tiwa', 'Loidmar Tibiwa'), ('Racia Muturumeliwa', 'Racia Muturumeliwa'), ('Elisa Ernesto', 'Elisa Ernesto')])
    classe = models.CharField('Classe e Turma', max_length=50, choices=[('8 classe, turma A', '8 classe, turma A')])
    valor = models.DecimalField(max_digits=10,  decimal_places=5, choices=[(2200, 2200)])
    mes = models.CharField('mês', choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'),
                                      ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Desembro', 'Desembro')], max_length=20)
    #email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome

class Comentario(models.Model):
    opiniao = models.TextField('opinão')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opiniao

class Informar(models.Model):
    #user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING)
    tema = models.CharField('Tema da informacão', max_length=50, null=True)
    info = models.TextField()

    def __str__(self):
        return self.tema




























 #   class Pagar(models.Model):
  #      user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
   # nome = models.CharField('Nome do aluno', max_length=20)
    #classe = models.CharField('Classe e Turma', max_length=20)
    #valor = models.DecimalField(max_digits=10, decimal_places=5)
    #mes = models.CharField('mês', choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'),
     #                                      ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Desembro', 'Desembro')], max_length=20)
    #email = models.EmailField(max_length=50)
    #user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING)
    #def __str__(self):
     #   return self.nome
