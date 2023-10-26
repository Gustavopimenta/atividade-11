from django.shortcuts import render
from .models import Aluno
from .forms import AlunoForm 


def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/cadastrar_aluno.html', {'form': form})

def visualizar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    return render(request, 'alunos/visualizar_aluno.html', {'aluno': aluno})

def editar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/editar_aluno.html', {'form': form, 'aluno': aluno})

def excluir_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    aluno.delete()
    return redirect('lista_alunos')


