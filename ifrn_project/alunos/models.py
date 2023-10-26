from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cidade = models.ForeignKey('cidades.Cidade', on_delete=models.CASCADE)
    curso = models.ForeignKey('cursos.Curso', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
