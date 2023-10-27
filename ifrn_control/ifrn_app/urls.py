from django.contrib import admin
from django.urls import path
from ifrn_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('visualizar_aluno/<int:id>/', views.visualizar_aluno, name='visualizar_aluno'),
    path('editar_aluno/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir_aluno/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]
