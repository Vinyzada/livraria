from django.contrib import admin

# Register your models here.
from .models import Editora, Categoria, Autor, Livro

admin.site.register(Editora)
admin.site.register(Categoria)
admin.site.register(Livro)
admin.site.register(Autor)
