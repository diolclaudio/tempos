from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Inscricoes(models.Model):
    nome= models.CharField('Nome do(a) aluno(a)', max_length=50)
    sexo= models.CharField('sexo', max_length=20, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'),])
    idade = models.DecimalField('idade', max_digits=2, decimal_places=0)
    nascimento_dia = models.DecimalField('dia de nascimento', max_digits=2, decimal_places=0)
    nascimento_mes = models.CharField('mês', choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'),
                                                      ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'),  ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Desembro', 'Desembro')], max_length=20)
    nascimento_ano = models.DecimalField('Ano de nascimento', max_digits=4, decimal_places=0)
    cell1 = models.DecimalField('Tel.nº', max_digits=9, decimal_places=0)
    cell2 = models.DecimalField('outro Tel.n', max_digits=9, decimal_places=0)
    #BI
    bi = models.DecimalField('Portador do B.I. Nº', max_digits=15, decimal_places=0)
    emitido = models.CharField('Emitido pelo Arquivo de', max_length=25)
    distrito = models.CharField('Distrito', max_length=20,)
    #provincia = models.CharField('Província de', max_length=15),

    #Redisencia
    bairro = models.CharField('Residente no bairro', max_length=20)
    celula = models.CharField('Célula', max_length=15)
    quarteirao = models.DecimalField('Quarteirão', max_digits=6, decimal_places=0)
    casa = models.DecimalField('Número de casa', max_digits=5, decimal_places=0)
    #Informacoes adicionais
    doenca = models.CharField('Sofre de alguma doença?',max_length=3, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO'),])
    qual_doenca = models.CharField('Em caso afirmativo indintifique a doença', max_length=15)

    #Filiação
    nome_pai = models.CharField('Nome do Pai', max_length=50, null=True)
    local_trabalho_pai = models.CharField('Local de trabalho do pai', max_length=50, null=True)
    profissao_pai = models.CharField('Profissão do pai', max_length=50, null=True)
    cell_pai = models.DecimalField('Telefone do pai', max_digits=9, decimal_places=0, null=True)
    nome_mae = models.CharField('Nome do Mãe', max_length=50,null=True)
    local_trabalho_mae = models.CharField('Local de trabalho do Mãe', max_length=50, null=True)
    profissao_mae = models.CharField('Profissão do Mãe', max_length=50, null=True)
    cell_mae = models.DecimalField('Telefone do Mãe', max_digits=9, decimal_places=0, null=True)

    #MAis informações
    classe = models.CharField('PRETENDE MATRICULAR-SE NA',max_length=9, choices=[('8ª', '8ª'), ('9ª', '9ª'), ('10ª', '10ª'), ('11ª', '11ª'), ('12ª', '12ª')], null=True)
    curso = models.CharField('No curso',max_length=10, choices=[('diurno', 'diurno'), ('noturno', 'noturno'),], null=True)

        #Prencheer apenas a 10 classe
    seccao = models.CharField('A preencher somente pelos alunos 10ª classe',max_length=18, choices=[('Todas Disc.', 'Tpdas Disc'), ('Secção de Letras', 'Secção de Letras'), ('Secção de Ciências', 'Secção de Ciências')], null=True)

         #Segundo ciclo
    grupo = models.CharField('Grupo',max_length=1, choices=[('A', 'A'), ('B', 'B'),], null=True)

        #Ano anteror
    anterior = models.CharField('No ano letivo anterir frequentou a',max_length=9, choices=[('7ª', '7ª'),('8ª', '8ª'), ('9ª', '9ª'), ('10ª', '10ª'), ('11ª', '11ª'), ('12ª', '12ª')], null=True)
    turma = models.CharField('Turma', max_length=3,null=True)
    aproveitamento = models.CharField("Aproveitamento do ano anterior", max_length=2, null=True)

class Pagar(models.Model):
    nome = models.CharField('Nome do aluno', max_length=20)
    classe = models.CharField('Classe e Turma', max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=5)
    mes = models.CharField('mês', choices=[('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'),
                                           ('Março', 'Março'), ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'), ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'), ('Outubro', 'Outubro'), ('Novembro', 'Novembro'), ('Desembro', 'Desembro')], max_length=20)
    email = models.EmailField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.nome

class Comentario(models.Model):
    opiniao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opiniao