from django import forms
from elearning.models import Etudiant, Enseignant, Cour


class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'email']
        widgets = { 'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
                    }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'email']
        widgets = { 'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
                    }

class CourForm(forms.ModelForm):

    enseignant: forms.ModelChoiceField(queryset=Enseignant.objects.all())
    class Meta:
        model = Cour
        fields = ['nom', 'code', 'enseignant']
        widgets = { 'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'code': forms.TextInput(attrs={ 'class': 'form-control' })
                    }