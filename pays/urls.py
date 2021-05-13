from django.urls import path
from . import views

app_name = 'pays'

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info, name='info'),
    path('comentario/', views.comentario, name='comentario'),
    #lista de pagamentos
    path('pay/', views.pagamentos, name='pagamentos'),

    #Classes que devem pasar
    path('oitava/pagar', views.oito, name='oito'),
    path('nove/pagar', views.nove, name='nove'),
    path('dez/pagar', views.dez, name='dez'),
    path('decima_primeira/pagar', views.primeira, name='primeira'),
    path('decima_segunda/pagar', views.segunda, name='segunda'),

    #Turmas para pagar
    path('oitava_a/', views.oitoa, name='oitoa'),

    path('listas/', views.listas, name='listas'),
    path('horarios/', views.hor, name='hor'),
    #Horarios
    path('oitava/', views.oita, name='oita'),
    path('nona/', views.nona, name='nona'),
    path('decima/', views.decima, name='decima'),
    path('onze/', views.onze, name='onze'),
    path('decima_segunda', views.doze, name='doze'),
]
