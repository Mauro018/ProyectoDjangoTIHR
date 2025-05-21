from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import User

html_base = """
<h1>Gangazos</h1>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/about">Sobre los Gangazos</a></li>
    <li><a href="/portafolio">Categorias en oferta</a></li>
    <li><a href="/contact">Contactenos</a></li>
    <li><a href="/productos">Productos</a></li>
    <li><a href="/login">Iniciar sesión</a></li>
    <li><a href="/logout">Cerrar sesión</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")

def portafolio(request):
    return render(request,"core/portafolio.html")

def productos(request):
    return render(request,"core/productos.html")

def contact(request):
    return render(request,"core/contact.html")

def Login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                return redirect('dashboard') # Redirecciona al panel de administración
            except User.DoesNotExist:
                error_message = "Usuario o contraseña incorrectos"
                return render(request, 'core/login.html', {'error_message': error_message})
    else:
        form = LoginForm()
    return render(request,'core/login.html', {'form': form})

def Logout_view(request):
    logout(request)
    return redirect('home')

def Dashboard_view(request):
    return render(request,'core/dashboard.html')