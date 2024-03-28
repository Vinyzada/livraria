from rest_framework.serializers import ModelSerializer

from livraria.models import Livro

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
