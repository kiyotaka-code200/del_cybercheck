from django.db import models

class CyberRecord(models.Model):
    CHOIX_NIVEAU = [
        ('L1', 'Licence 1'), ('L2', 'Licence 2'), ('L3', 'Licence 3'),
        ('M1', 'Master 1'), ('M2', 'Master 2'), ('D', 'Doctorat'),
    ]

    CHOIX_OS = [
        ('parrot', 'Parrot OS / Kali Linux'),
        ('windows', 'Windows'),
        ('macos', 'macOS'),
        ('android', 'Android/iOS'),
    ]


    nom = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    ville = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    

    niveau_etudes = models.CharField(max_length=5, choices=CHOIX_NIVEAU)
    os_principal = models.CharField(max_length=10, choices=CHOIX_OS)
    
    utilise_2fa = models.BooleanField(default=False, verbose_name="Double Authentification")
    gestionnaire_mdp = models.BooleanField(default=False, verbose_name="Gestionnaire de MDP")
    maj_auto = models.BooleanField(default=False, verbose_name="Mises à jour automatiques")

    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.ville}"