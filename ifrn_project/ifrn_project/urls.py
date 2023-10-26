from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_alunos, name='lista_alunos'),
    path('editar/<int:aluno_id>/', views.editar_aluno, name='editar_aluno'),
    path('salvar/<int:aluno_id>/', views.salvar_alteracoes, name='salvar_alteracoes'),
    
]
