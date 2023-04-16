from django import forms
from elearning.models import Etudiant, Enseignant, Cour,Inscri,Module, Formation, Group


class EtudiantForm(forms.ModelForm):

    group: forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email','cne','group']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'cne': forms.TextInput(attrs={'class': 'form-control'}),

                    }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'email','cni']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'cni': forms.TextInput(attrs={'class': 'form-control'})
                    }

class CourForm(forms.ModelForm):

    module: forms.ModelChoiceField(queryset=Module.objects.all())
    class Meta:
        model = Cour
        fields = ['nom', 'format','module']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'format': forms.TextInput(attrs={ 'class': 'form-control' })
                    }
class ModuleForm(forms.ModelForm):
    formation: forms.ModelChoiceField(queryset=Formation.objects.all())
    enseignant: forms.ModelChoiceField(queryset=Enseignant.objects.all())
    class Meta:
        model = Module
        fields = ['nom','formation','enseignant']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
                    }
class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
                    }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['nom','nbrEtudiant']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'nbrEtudiant': forms.NumberInput(attrs={'class': 'form-control'}),
                    }

class InscriForm(forms.ModelForm):

        Cour: forms.ModelChoiceField(queryset=Cour.objects.all())
        Etudiant: forms.ModelChoiceField(queryset=Etudiant.objects.all())
        class Meta:
         model = Inscri
         fields = ['cour', 'etudiant']
