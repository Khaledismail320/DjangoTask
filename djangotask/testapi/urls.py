from django.urls import path, include
from . import views


urlpatterns = [
    path('createUser/', views.createUser),
    path('getUser/', views.getUser),
    path("deleteUser/", views.deleteUser),
    path('updateUser/',views.updateUser),
    
]