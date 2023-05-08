from django.db import models

# Create your models here.
from django.db import models


class Formation(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom}"

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cin = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f"{self.nom}"

class Group(models.Model):
    nom = models.CharField(max_length=100)
    nbrEtudiant = models.IntegerField()
    def __str__(self):
        return f"{self.nom}"

class Module(models.Model):
    nom = models.CharField(max_length=100)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    nbrCour = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom}"

class Cour(models.Model):
    nom = models.CharField(max_length=100)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null = True)
    def __str__(self):
        return f"{self.nom}"


class Etudiant(models.Model):

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    cne = models.CharField(max_length=100)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    username = models.CharField(max_length=30,default='',unique='true')
    password = models.CharField(max_length=30, default='')

    def __str__(self):
        return f"{self.nom}"

class Contenu(models.Model):
    description = models.TextField(max_length=10000)
    format = models.CharField(max_length=200)
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description,self.cour}"
