from django.db import models

# Create your models here.


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.PositiveBigIntegerField(max_length=11)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autors"

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
