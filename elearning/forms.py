from django import forms
from elearning.models import Etudiant, Enseignant, Cour,Inscri


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email','cne']
        widgets = { 'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'cne': forms.TextInput(attrs={'class': 'form-control'}),
                    }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'email','cni']
        widgets = { 'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'cni': forms.TextInput(attrs={'class': 'form-control'}),
                    }

class CourForm(forms.ModelForm):

    enseignant: forms.ModelChoiceField(queryset=Enseignant.objects.all())
    class Meta:
        model = Cour
        fields = ['nom', 'code', 'enseignant']
        widgets = { 'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'code': forms.TextInput(attrs={ 'class': 'form-control' })
                    }

class InscriForm(forms.ModelForm):

        Cour: forms.ModelChoiceField(queryset=Cour.objects.all())
        Etudiant: forms.ModelChoiceField(queryset=Etudiant.objects.all())
        class Meta:
         model = Inscri
         fields = ['cour', 'etudiant']
