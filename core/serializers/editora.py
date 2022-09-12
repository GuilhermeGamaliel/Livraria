from rest_framework.serializers import ModelSerializer

from Livraria.core import Autor, Categoria, Editora, Livro


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"