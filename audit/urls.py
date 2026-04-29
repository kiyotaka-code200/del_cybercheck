from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Ta page avec le formulaire
    path('resultats/', views.resultats, name='resultats'), # Ta page de stats
]