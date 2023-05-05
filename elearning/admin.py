from django.contrib import admin
from .models import Etudiant,Enseignant,Formation,Cour,Module,Group
# Register your models here.
@admin.register(Etudiant)
class adminEtudiant(admin.ModelAdmin):
    list_display = ('nom','prenom','cne','email')
    ordering =('nom',)
    search_fields =('cne',)

@admin.register(Enseignant)
class adminEnseignant(admin.ModelAdmin):
    list_display = ('nom','prenom','cin','email')
    ordering =('nom',)
    search_fields =('cin',)
@admin.register(Formation)
class adminFormation(admin.ModelAdmin):
    list_display = ('nom',)
    ordering =('nom',)
    search_fields =('nom',)

@admin.register(Cour)
class adminCour(admin.ModelAdmin):
    list_display = ('nom','formation','module')
    ordering = ('nom',)
    search_fields = ('nom',)

@admin.register(Module)
class adminModule(admin.ModelAdmin):
    list_display = ('nom', 'formation', 'enseignant','nbrCour')
    ordering = ('nom',)
    search_fields = ('nom',)

@admin.register(Group)
class adminGroup(admin.ModelAdmin):
    list_display = ('nom', 'nbrEtudiant',)
    ordering = ('nom',)
    search_fields = ('nom',)