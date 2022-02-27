from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('delete/<str:pk>',views.deleteSubject, name="delete"),
   path('update/<str:pk>',views.updateSubject, name="update")  
]