from rest_framework.serializers import ModelSerializer

from Livraria.core import Autor, Categoria, Editora, Livro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"