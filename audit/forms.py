from django import forms

class AuditForm(forms.Form):
    # Liste de choix pour le menu déroulant du genre
    GENRE_CHOICES = [
        ('', '--- Choisir votre genre ---'),
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('Autre', 'Autre'),
    ]

    # --- Champs Texte ---
    nom_utilisateur = forms.CharField(
        label="Votre Pseudo", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: CyberPro2024'})
    )
    
    nationalite = forms.CharField(
        label="Nationalité", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Camerounaise'})
    )

    # --- Champ de sélection (Menu déroulant) ---
    genre = forms.ChoiceField(
        label="Genre",
        choices=GENRE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # --- Champs Booléens (Cases à cocher) ---
    has_phone_password = forms.BooleanField(
        label="Avez-vous un mot de passe/schéma sur votre téléphone ?", 
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    use_2fa = forms.BooleanField(
        label="Utilisez-vous la double authentification (2FA) ?", 
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    
    use_manager = forms.BooleanField(
        label="Utilisez-vous un gestionnaire de mots de passe ?", 
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )