from django.contrib import admin
from .models import Autor, Libro


class AutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'email', 'bio']
    search_fields = ['nombre', 'email']


class LibroAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'autor', 'fecha_publicacion']
    search_fields = ['title', 'autor__nombre']
    list_filter = ['fecha_publicacion']


admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
