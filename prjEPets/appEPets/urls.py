from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('add', views.addPet, name="add"),
    path('pet/<str:pk>/', views.detailPet, name="detail"),
]

#path('update/<str:pk>/', views.updatePet, name="update"),
#path('delete/<str:pk>/', views.deletePet, name="delete"),
#path('adot/<str:pk>', views.adotPet, name="adot"),