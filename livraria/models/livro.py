from django.db import models
from livraria.models import Autor, Categoria, Editora

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(
        default=0, max_digits=7, null=True, blank=True, decimal_places=2)

    def __str__(self):
        return f"{self.titulo} ({self.quantidade})"

    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros")
    
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros")
    
    autores = models.ManyToManyField(Autor, related_name="livros")