from django import forms

class AuditForm(forms.Form):
    nom_utilisateur = forms.CharField(
        label="Votre Pseudo", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: CyberPro2024'})
    )
    use_2fa = forms.BooleanField(
        label="Utilisez-vous la double authentification ?", 
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    use_manager = forms.BooleanField(
        label="Utilisez-vous un gestionnaire de mots de passe ?", 
        required=False, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )