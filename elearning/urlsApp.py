from django.urls import path

from . import views
from .views import etudiant_list, enseignant_list, cour_list, inscri_list, addnewEtudiant,update,edit,addnewEnseignant,editEnseignant,updateEnseignant,deleteEnseignant,addnewCour

urlpatterns = [
    #path('products/', product_list, name='product_list'),
    path('etudiant/', etudiant_list, name='etudiant_list'),
    path('enseignant/', enseignant_list, name='enseignant_list'),
    path('cour/', cour_list, name='cour_list'),
    path('inscription/', inscri_list, name='inscri_list'),
    path('add/', addnewEtudiant, name='addnewEtudiant'),
    path("addnew", views.addnewEtudiant, name="addnew"),
    path("editEtudiant/<int:id>", edit, name="edit"),
    path("update/<int:id>", update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("addnewenseignant", views.addnewEnseignant, name="addnewenseignant"),
    path("editEnseignant/<int:id>", editEnseignant, name="editEnseignant"),
    path("updateEnseignant/<int:id>", updateEnseignant, name="updateEnseignant"),
    path("deleteEnseignant/<int:id>", views.deleteEnseignant, name="deleteEnseignant"),
    path('addCour', addnewCour, name='addnewCour'),
    path("editCour/<int:id>", views.editCour, name="editCour"),
    path("updateCour/<int:id>", views.updateCour, name="updateCour"),
    path("deleteCour/<int:id>", views.deleteCour, name="deleteCour"),
    path("addnewinscri", views.addnewInscri, name="addnewInscri"),
    path("editInscri/<int:id>", views.editInscri, name="editInscri"),
    path("updateInscri/<int:id>", views.updateInscri, name="updateInscri"),
    path("deleteInscri/<int:id>", views.deleteInscri, name="deleteInscri"),


]