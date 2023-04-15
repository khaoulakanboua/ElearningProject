from django.db import models

# Create your models here.
from django.db import models


class Formation(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cne = models.CharField(max_length=100)
    
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Group(models.Model):
    nom = models.CharField(max_length=100)
    nbrEtudiant = models.CharField(max_length=100)


    def __str__(self):
        return self.nom

class Module(models.Model):
    nom = models.CharField(max_length=100)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom




class Cour(models.Model):
    nom = models.CharField(max_length=100)
    format = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom



class Etudiant(models.Model):

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    cni = models.CharField(max_length=100)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Inscri(models.Model):
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.etudiant.nom} inscrit au cours {self.cour.nom}"