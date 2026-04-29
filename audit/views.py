from django.shortcuts import render, redirect
from .forms import AuditForm 
from .models import AuditData  

def home(request):
    if request.method == "POST":
        form = AuditForm(request.POST)
        if form.is_valid():
            # --- SAUVEGARDE DANS LA BASE DE DONNÉES ---
            AuditData.objects.create(
                nom_utilisateur=form.cleaned_data['nom_utilisateur'],
                nationalite=form.cleaned_data['nationalite'],
                genre=form.cleaned_data['genre'],
                has_phone_password=form.cleaned_data['has_phone_password'],
                use_2fa=form.cleaned_data['use_2fa'],
                use_manager=form.cleaned_data['use_manager']
            )
            return redirect('resultats')
    else:
        form = AuditForm()
    
    return render(request, 'audit/home.html', {'form': form})

def resultats(request):
    # --- CALCUL DES VRAIES STATISTIQUES ---
    total = AuditData.objects.count() 
    
    if total > 0:
        count_2fa = AuditData.objects.filter(use_2fa=True).count()
        count_mdp = AuditData.objects.filter(has_phone_password=True).count()
        
        pct_2fa = (count_2fa / total) * 100
        pct_mdp = (count_mdp / total) * 100
    else:
        pct_2fa = 0
        pct_mdp = 0

    context = {
        'total': total,
        'pct_2fa': round(pct_2fa, 1), 
        'pct_mdp': round(pct_mdp, 1),
    }
    return render(request, 'audit/resultats.html', context)