from django.db import models

# Create your models here.
from django.db import models

class Etudiant(models.Model):
    #id_coun=models.IntegerField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Cour(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Inscri(models.Model):
    cour = models.ForeignKey(Cour, on_delete=models.CASCADE)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.etudiant.nom} inscrit au cours {self.cour.nom}"