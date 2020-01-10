from django.urls import path
from .views import Home, DetallePost,Generales,Programacion,Tecnologia,Tutoriales,Gaming

urlpatterns = [
    path('',Home, name = 'index'),
    path('generales/',Generales, name = 'generales'),
    path('programacion/',Programacion, name = 'programacion'),
    path('tecnologia/',Tecnologia, name = 'tecnologia'),
    path('tutoriales/',Tutoriales, name = 'tutoriales'),
    path('gaming/',Gaming, name = 'gaming'),
    path('<slug:slug>/',DetallePost, name = 'detallepost'),
]
