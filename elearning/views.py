from django.shortcuts import render, redirect
from elearning.forms import EtudiantForm, EnseignantForm, CourForm,InscriForm

# Create your views here.
from .models import Etudiant,Enseignant,Cour,Inscri
def etudiant_list(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiant_list.html', {'etudiants': etudiants})

def enseignant_list(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'enseignant_list.html', {'enseignants': enseignants})

def cour_list(request):
    cours = Cour.objects.all()
    return render(request, 'cour_list.html', {'cours': cours})

def inscri_list(request):
    inscriptions = Inscri.objects.all()
    return render(request, 'inscri_list.html', {'inscriptions': inscriptions})

def addnewEtudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('etudiant/')
            except:
                pass
    else:
        form = EtudiantForm()
    return render(request,'Add.html',{'form':form})


def edit(request, id):
    etudiant = Etudiant.objects.get(id=id)
    return render(request,'editEtudiant.html', {'etudiant':etudiant})

def update(request, id):
    etudiant = Etudiant.objects.get(id=id)
    form = EtudiantForm(request.POST, instance = etudiant)
    if form.is_valid():
        form.save()
        return redirect("/etudiant")
    return render(request, 'editEtudiant.html', {'etudiant': etudiant})
def delete(request, id):
    etudiant = Etudiant.objects.get(id=id)
    etudiant.delete()
    return redirect("/etudiant")

def addnewEnseignant(request):
    if request.method == "POST":
        form = EnseignantForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('enseignant/')
            except:
                pass
    else:
        form = EtudiantForm()
    return render(request,'addEnseignant.html',{'form':form})

def editEnseignant(request, id):
    enseignant = Enseignant.objects.get(id=id)
    return render(request,'editEnseignant.html', {'enseignant':enseignant})

def updateEnseignant(request, id):
    enseignant = Enseignant.objects.get(id=id)
    form = EnseignantForm(request.POST, instance = enseignant)
    if form.is_valid():
        form.save()
        return redirect("/enseignant")
    return render(request, 'editEnseignant.html', {'enseignant': enseignant})
def deleteEnseignant(request, id):
    enseignant = Enseignant.objects.get(id=id)
    enseignant.delete()
    return redirect("/enseignant")

def addnewCour(request):
    if request.method == "POST":
        form = CourForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('cour/')
            except:
                pass
    else:
        form = CourForm()
    return render(request,'addCour.html',{'form':form})



def editCour(request, id):
    cour =Cour.objects.get(id=id)
    return render(request,'editCour.html', {'cour':cour})

def updateCour(request, id):
    cour = Cour.objects.get(id=id)
    form = CourForm(request.POST, instance = cour)
    if form.is_valid():
        form.save()
        return redirect("/cour")
    return render(request, 'editCour.html', {'cour': cour})
def deleteCour(request, id):
    cour = Cour.objects.get(id=id)
    cour.delete()
    return redirect("/cour")
def addnewInscri(request):
    if request.method == "POST":
        form = InscriForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('inscription/')
            except:
                pass
    else:
        form = InscriForm()
    return render(request,'addInscri.html',{'form':form})

def editInscri(request, id):
    inscription = Inscri.objects.get(id=id)
    return render(request,'editInscri.html', {'inscription':inscription})

def updateInscri(request, id):
    inscription = Inscri.objects.get(id=id)
    form = InscriForm(request.POST, instance = inscription)
    if form.is_valid():
        form.save()
        return redirect("/inscription")
    return render(request, 'editInscri.html', {'inscription': inscription})
def deleteInscri(request, id):
    inscription = Inscri.objects.get(id=id)
    inscription.delete()
    return redirect("/inscription")