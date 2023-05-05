from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from elearning.forms import EtudiantForm, EnseignantForm, CourForm, FormationForm, GroupForm, LoginForm
from .forms import EtudiantForm
from django import forms
from django.core import validators
from django.contrib import messages


# Create your views here.
from .models import Etudiant, Enseignant, Cour, Formation, Group, Module, Contenu

# =========================================View Display Cours=================================================================
class CoursDisplayView:
    def coursdisplay(request):
        cours = Cour.objects.all()
        contenus = Contenu.objects.all()

        return render(request, 'Cours_display.html', {'contenus': contenus})
# =========================================View Etudiant=================================================================
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
                    return redirect('/')
                except:
                    pass
        else:
            form = EtudiantForm()
        return render(request, 'register2.html', {'form': form})

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


# =========================================View Enseignant==========================================================
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
        return render(request, 'Add.html', {'form': form})

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


# =========================================View Cours=================================================================
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
        return render(request, 'Add.html', {'form': form})

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


# =========================================View Module=================================================================
class ModuleView:
    def modules(request):
        etudiant = Etudiant.objects.get(username=request.session.get('username'))
        modules = Module.objects.raw("""
                    SELECT elearning_module.*, COUNT(elearning_cour.id) as nbrCours
                    FROM elearning_module
                    LEFT JOIN elearning_cour ON elearning_cour.module_id = elearning_module.id
                    WHERE elearning_module.formation_id = %s
                    GROUP BY elearning_module.id
                """, [etudiant.formation_id])

        return render(request, 'modules.html', {'modules': modules})

# =========================================View Formation=================================================================
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
        return render(request, 'Add.html', {'form': form})

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


# ========================================View Group==========================================================================
class GroupView:
    def group_list(request):
        groups = Group.objects.all()
        return render(request, 'groupList.html', {'groups': groups})

    def addnewGroup(request):
        if request.method == "POST":
            form = GroupForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('group/')
                except:
                    pass
        else:
            form = GroupForm()
        return render(request, 'Add.html', {'form': form})

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

# ========================================View Login================================================================


class LoginView:

    def login(request):
        error_messages = []

        if request.method == 'POST':
            form = LoginForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                if Etudiant.objects.filter(username=username, password=password).exists():
                    request.session['username'] = username
                    return redirect('/etudiant')

                else:
                    error_messages.append('Invalid login credentials.')
            else:
                error_messages.append('Invalid form data.')
        else:
            form = LoginForm()

        context = {'form': form, 'error_messages': error_messages}
        return render(request, 'login_page2.html',context)

def home(request):
    return render(request, 'index.html')


def profile(request):
    if request.session['username'] == request.session.get('username'):
        etudiant = Etudiant.objects.get(username=request.session.get('username'))
        return render(request, 'profile.html', {'etudiant': etudiant})
    else:
        return redirect('/')
    print(request.session.get('username'))

    return render(request, 'profile.html')

def updateProfile(request):
        etudiant = Etudiant.objects.get(username=request.session.get('username'))
        form = EtudiantForm(request.POST, instance=etudiant)
        if request.method == 'POST':
            etudiant.username = request.POST['username']
            etudiant.prenom = request.POST['prenom']
            etudiant.nom = request.POST['nom']
            etudiant.email = request.POST['email']
            etudiant.cne = request.POST['cne']
            etudiant.save()
            return redirect("/")
        return render(request, 'profile.html', {'etudiant': etudiant})



def password(request):
    if request.session.get('username'):
        etudiant = Etudiant.objects.get(username=request.session['username'])
        return render(request, 'password.html', {'etudiant': etudiant})
    else:
        return redirect('/')

def changePassword(request):
    if request.session.get('username'):
        etudiant = Etudiant.objects.get(
            username=request.session['username'])
        if request.method == 'POST':
            if etudiant.password == request.POST['oldPassword']:
                # New and confirm password check is done in the client side
                etudiant.password = request.POST['newPassword']
                etudiant.save()
                messages.success(request, 'Password was changed successfully')
                return redirect('/profile')
            else:
                messages.error(
                    request, 'Password is incorrect. Please try again')
                return redirect('/password')
        else:
            return render(request, 'password.html', {'etudiant': etudiant})
    else:
        return redirect('/')














