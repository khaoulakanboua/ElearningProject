from django.urls import path
from . import views
from .views import  inscri_list,home

urlpatterns = [
    #path('products/', product_list, name='product_list'),
    path('home/', home, name='home'),
   #path('add/', views.EtudiantView.addnewEtudiant, name='addnewEtudiant'),
    path('etudiant/', views.EtudiantView.etudiant_list, name='etudiant_list'),
    path("addnewetudiant", views.EtudiantView.addnewEtudiant, name="addnewEtudiant"),
    path("editEtudiant/<int:id>", views.EtudiantView.editEtudiant, name="editEtudiant"),
    path("update/<int:id>", views.EtudiantView.updateEtudiant, name="update"),
    path("delete/<int:id>", views.EtudiantView.deleteEtudiant, name="delete"),
    #=====================================================================================
    path('enseignant/',views.EnseignantView.enseignant_list, name='enseignant_list'),
    path("addnewenseignant", views.EnseignantView.addnewEnseignant, name="addnewenseignant"),
    path("editEnseignant/<int:id>", views.EnseignantView.editEnseignant, name="editEnseignant"),
    path("updateEnseignant/<int:id>", views.EnseignantView.updateEnseignant, name="updateEnseignant"),
    path("deleteEnseignant/<int:id>", views.EnseignantView.deleteEnseignant, name="deleteEnseignant"),
    # =====================================================================================
    path('formation/', views.FormationView.formation_list, name='formation_list'),
    path("addnewformation", views.FormationView.addnewFormation, name="addnewFormation"),
    path("editFormation/<int:id>", views.FormationView.editFormation, name="addnewFormation"),
    path("updateFormation/<int:id>", views.FormationView.updateFormation, name="updateFormation"),
    path("deleteFormation/<int:id>", views.FormationView.deleteFormation, name="deleteFormation"),
    # =====================================================================================
    path('group/', views.GroupView.group_list, name='group_list'),
    path("addnewgroup", views.GroupView.addnewGroup, name="addnewGroup"),
    path("editGroup/<int:id>", views.GroupView.editGroup, name="editGroup"),
    path("updateGroup/<int:id>", views.GroupView.updateGroup, name="updateGroup"),
    path("deleteGroup/<int:id>", views.GroupView.deleteGroup, name="deleteGroup"),

    #=====================================================================================
    #path('cour/', views.CoursView.cour_list, name='cour_list'),
    #path('addCour', addnewCour, name='addnewCour'),
    #path("editCour/<int:id>", views.editCour, name="editCour"),
    ##path("updateCour/<int:id>", views.updateCour, name="updateCour"),
    #path("deleteCour/<int:id>", views.deleteCour, name="deleteCour"),
    #=====================================================================================
    #path('inscription/', inscri_list, name='inscri_list'),
    #path("addnewinscri", views.addnewInscri, name="addnewInscri"),
    #path("editInscri/<int:id>", views.editInscri, name="editInscri"),
    #path("updateInscri/<int:id>", views.updateInscri, name="updateInscri"),
    #path("deleteInscri/<int:id>", views.deleteInscri, name="deleteInscri"),


]