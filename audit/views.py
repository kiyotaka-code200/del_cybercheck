from django.shortcuts import render, redirect
from .forms import AuditForm # On va créer ce fichier juste après

def home(request):
    if request.method == "POST":
        form = AuditForm(request.POST)
        if form.is_valid():
            # Ici, on simule l'enregistrement (on verra la DB plus tard)
            # On passe les données à la page résultats via la session ou directement
            return redirect('resultats')
    else:
        form = AuditForm()
    
    return render(request, 'audit/home.html', {'form': form})

def resultats(request):
    # On simule des statistiques pour l'instant pour ton template
    context = {
        'total': 15,
        'pct_2fa': 65,
        'pct_mdp': 40,
    }
    return render(request, 'audit/resultats.html', context)