from django.contrib import admin
from django.urls import path, include # N'oublie pas d'ajouter include ici

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('audit.urls')), # Cela connecte ton app audit à la racine du site
]
