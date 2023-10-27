from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    email = models.EmailField()
    data_nascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return self.nome
