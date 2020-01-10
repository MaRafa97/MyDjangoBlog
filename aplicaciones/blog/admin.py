from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class CategoriaResource(resources.ModelResource): #hace funcionar la opcion de importar y exportar
    class Meta:
        model = Categoria


class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):#agrega la herencia de import export
    search_fields = ['nombre'] #activa la barra de busqueda
    list_display = ['nombre','estado','fecha_creacion'] #sobreescribe la lista
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource): #hace funcionar la opcion de importar y exportar
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']#los parametros es la busqueda
    list_display = ['nombres','apellidos','correo','estado','fecha_creacion']
    resource_class = AutorResource

class PostResource(resources.ModelResource): #hace funcionar la opcion de importar y exportar
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','slug','Descripcion']#los parametros es la busqueda
    list_display = ['titulo','slug','Descripcion','fecha_creacion']
    resource_class = PostResource

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
