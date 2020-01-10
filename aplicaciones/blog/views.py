from django.shortcuts import render
from django.shortcuts import get_object_or_404 #funcion que valida si existe o no pagina
from django.db.models import Q #permite realizar busquedas con multiples valores de filtro
from django.core.paginator import Paginator #paginador
from .models import *

# Create your views here.
def Home(request):
    queryset = request.GET.get("buscar")#trae la palabra a buscar con el cuadro de busqueda
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(Descripcion__icontains = queryset) #se trae uno u otro,icontains indica que contenga la palabra
        ).distinct()#no se trae todo, solo la primer opcion que encuentra

    paginator = Paginator(posts,2)#pasa la lista de post y la cantidad de elementos por pagina
    page = request.GET.get('page')#saber en que pagina nos encontramos
    posts = paginator.get_page(page)#obtiene los posts por pagina

    return render(request,'index.html',{'posts':posts})

def Generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'General'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(Descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'General')
        ).distinct()

    paginator = Paginator(posts,2)#pasa la lista de post y la cantidad de elementos por pagina
    page = request.GET.get('page')#saber en que pagina nos encontramos
    posts = paginator.get_page(page)#obtiene los posts por pagina

    return render(request,'generales.html',{'posts':posts})

def Programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Programacion'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(Descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
        ).distinct()

    paginator = Paginator(posts,2)#pasa la lista de post y la cantidad de elementos por pagina
    page = request.GET.get('page')#saber en que pagina nos encontramos
    posts = paginator.get_page(page)#obtiene los posts por pagina

    return render(request,'programacion.html',{'posts':posts})

def Tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(Descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
            ).distinct()

    paginator = Paginator(posts,2)#pasa la lista de post y la cantidad de elementos por pagina
    page = request.GET.get('page')#saber en que pagina nos encontramos
    posts = paginator.get_page(page)#obtiene los posts por pagina

    return render(request,'tutoriales.html',{'posts':posts})

def Tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(Descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
            ).distinct()

    paginator = Paginator(posts,2)#pasa la lista de post y la cantidad de elementos por pagina
    page = request.GET.get('page')#saber en que pagina nos encontramos
    posts = paginator.get_page(page)#obtiene los posts por pagina

    return render(request,'tecnologia.html',{'posts':posts})

def Gaming(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__exact = 'Gaming'))
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(Descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__exact = 'Gaming')
            ).distinct()

    paginator = Paginator(posts,2)#pasa la lista de post y la cantidad de elementos por pagina
    page = request.GET.get('page')#saber en que pagina nos encontramos
    posts = paginator.get_page(page)#obtiene los posts por pagina
    
    return render(request,'gaming.html',{'posts':posts})

def DetallePost(request,slug):
    post = get_object_or_404(Post, slug = slug)#validamos que el objeto con el slug exista
    return render(request,'post.html',{'detalle_post':post})
