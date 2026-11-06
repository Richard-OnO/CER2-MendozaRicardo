from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Mascota, Especie

def home(request):
    return render(request, 'refugio/home.html')

def lista_mascotas(request):
    especie_id = request.GET.get('especie')
    
    if especie_id:
        mascotas = Mascota.objects.filter(especie_id=especie_id)
    else:
        mascotas = Mascota.objects.all()
        
    especies = Especie.objects.all()
    return render(request, 'refugio/catalogo.html', {'mascotas': mascotas, 'especies': especies})

def detalle_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk) 
    return render(request, 'refugio/detalle_mascota.html', {'mascota': mascota})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'refugio/login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def gestion_mascotas(request):
    return render(request, 'refugio/gestion.html')
