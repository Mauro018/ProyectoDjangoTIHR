from django.shortcuts import render,HttpResponse

html_base = """
<h1>Gangazos</h1>
<ul>
    <li><a href="/">Inicio</a></li>
    <li><a href="/about">Sobre los Gangazos</a></li>
    <li><a href="/portafolio">Categorias en oferta</a></li>
    <li><a href="/contact">Contactenos</a></li>
    <li><a href="/productos">Productos</a></li>
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