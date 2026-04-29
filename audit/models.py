from django.db import models

class CyberRecord(models.Model):
    
    nom_utilisateur = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    
    
    has_phone_password = models.BooleanField(default=False)
    use_2fa = models.BooleanField(default=False)
    use_manager = models.BooleanField(default=False)
    
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom_utilisateur} - {self.nationalite}"