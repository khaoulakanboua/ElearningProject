from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from elearning.forms import EtudiantForm, EnseignantForm,InscriForm, CourForm,FormationForm,GroupForm

# Create your views here.
from .models import Etudiant,Enseignant,Cour,Inscri,Formation,Group

#=========================================View Etudiant=================================================================
class EtudiantView:
    def etudiant_list(request):
        etudiants = Etudiant.objects.all()
        return render(request, 'etudiant_list.html', {'etudiants': etudiants})
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
        return render(request, 'Add.html', {'form': form})

    def editEtudiant(request, id):
        etudiant = Etudiant.objects.get(id=id)
        return render(request, 'editEtudiant.html', {'etudiant': etudiant})

    def updateEtudiant(request, id):
        etudiant = Etudiant.objects.get(id=id)
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            return redirect("/etudiant")
        return render(request, 'editEtudiant.html', {'etudiant': etudiant})

    def deleteEtudiant(request, id):
        etudiant = Etudiant.objects.get(id=id)
        etudiant.delete()
        return redirect("/etudiant")
#=========================================View Enseignant==========================================================
class EnseignantView:
    def enseignant_list(request):
        enseignants = Enseignant.objects.all()
        return render(request, 'enseignant_list.html', {'enseignants': enseignants})
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
            form = EnseignantForm()
        return render(request, 'addEnseignant.html', {'form': form})

    def editEnseignant(request, id):
        enseignant = Enseignant.objects.get(id=id)
        return render(request, 'editEnseignant.html', {'enseignant': enseignant})

    def updateEnseignant(request, id):
        enseignant = Enseignant.objects.get(id=id)
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect("/enseignant")
        return render(request, 'editEnseignant.html', {'enseignant': enseignant})

    def deleteEnseignant(request, id):
        enseignant = Enseignant.objects.get(id=id)
        enseignant.delete()
        return redirect("/enseignant")
#=========================================View Cours=================================================================
class CoursView:
    def cour_list(request):
        cours = Cour.objects.all()
        return render(request, 'cour_list.html', {'cours': cours})
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
        return render(request, 'addCour.html', {'form': form})
    def editCour(request, id):
        cour = Cour.objects.get(id=id)
        return render(request, 'editCour.html', {'cour': cour})
    def updateCour(request, id):
        cour = Cour.objects.get(id=id)
        form = CoursView(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/cour")
        return render(request, 'editCour.html', {'cour': cour})
    def deleteCour(request, id):
        cour = Cour.objects.get(id=id)
        cour.delete()
        return redirect("/cour")
#=========================================View Module=================================================================

#=========================================View Formation=================================================================
class FormationView:
    def formation_list(request):
        formations = Formation.objects.all()
        return render(request, 'formationList.html', {'formations': formations})
    def addnewFormation(request):
        if request.method == "POST":
            form = FormationForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('formation/')
                except:
                    pass
        else:
            form = FormationForm()
        return render(request, 'addFormation.html', {'form': form})

    def editFormation(request, id):
        formation = Formation.objects.get(id=id)
        return render(request, 'editFormation.html', {'formation': formation})

    def updateFormation(request, id):
        formation = Formation.objects.get(id=id)
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            return redirect("/formation")
        return render(request, 'editFormation.html', {'formation': formation})

    def deleteFormation(request, id):
        formation = Formation.objects.get(id=id)
        formation.delete()
        return redirect("/formation")

#========================================View Group==========================================================================
class GroupView:
        def group_list(request):
            groups = Group.objects.all()
            return render(request, 'groupList.html', {'groups': groups})

        def addnewGroup(request):
            if request.method == "POST":
                form =GroupForm(request.POST)
                if form.is_valid():
                    try:
                        form.save()
                        return redirect('group/')
                    except:
                        pass
            else:
                form =GroupForm()
            return render(request, 'addGroup.html', {'form': form})

        def editGroup(request, id):
            group = Group.objects.get(id=id)
            return render(request, 'editGroup.html', {'group': group})

        def updateGroup(request, id):
            group = Group.objects.get(id=id)
            form = GroupForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                return redirect("/group")
            return render(request, 'ediGroup.html', {'group': group})

        def deleteGroup(request, id):
            group = Group.objects.get(id=id)
            group.delete()
            return redirect("/group")


def home(request):
    return render(request, 'index.html')



def inscri_list(request):
    inscriptions = Inscri.objects.all()
    return render(request, 'inscri_list.html', {'inscriptions': inscriptions})
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