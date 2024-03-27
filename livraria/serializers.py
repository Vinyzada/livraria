from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora, Livro, Autor

#Categorias
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

#Editoras
class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

#Autores
class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

#Livros
class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ["id", "titulo", "preco"]

class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
