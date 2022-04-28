from venv import create
from django.contrib import admin
from django.urls import path
from . import views

app_name = "informations"

urlpatterns = [
    path('dashboard/', views.dashboard,name="dashboard"),
    path('addinfo/', views.addinfo,name="addinfo"),
    path('information/<int:id>', views.detail,name="detail"),
    path('update/<int:id>', views.updateInformation,name="update"),
    path('delete/<int:id>', views.deleteInformation,name="delete"),
    path('', views.informations,name="informations"),
    path('addmylist/<int:id>', views.addmylist,name="addmylist"),
]
