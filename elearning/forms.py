from django import forms
from elearning.models import Etudiant, Enseignant, Cour,Module, Formation, Group

class LoginForm(forms.Form):
    username = forms.CharField(label='UserName', max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

class EtudiantForm(forms.ModelForm):

    group: forms.ModelChoiceField(queryset=Group.objects.all())
    formation: forms.ModelChoiceField(queryset=Formation.objects.all())
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom','username','password', 'email','cne','group','formation']
        widgets = {
            'nom': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your name', 'id': 'nom-input'}),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' , 'placeholder': 'Enter your prenom', 'id': 'nom-input'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'id': 'nom-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'id': 'nom-input'}),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' , 'placeholder': 'Enter your email', 'id': 'nom-input'}),
            'cne': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your cne', 'id': 'nom-input'}),

                    }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'email','cin']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'prenom': forms.TextInput(attrs={ 'class': 'form-control' }),
            'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            'cin': forms.TextInput(attrs={'class': 'form-control'})
                    }

class CourForm(forms.ModelForm):

    module: forms.ModelChoiceField(queryset=Module.objects.all())
    formation: forms.ModelChoiceField(queryset=Formation.objects.all())

    class Meta:
        model = Cour
        fields = ['nom', 'formation','module']
        widgets = {
            'nom': forms.TextInput(attrs={ 'class': 'form-control' }),
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
