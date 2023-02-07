from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from pokemon.models import Pokemon
from pokemon.serializer import PokemonSerializer

# Only allow filtering on columns
VALID_PARAMS = [field.name for field in Pokemon._meta.get_fields()]


class PokemonCollectionView(generics.ListCreateAPIView):
    http_method_names = ["get", "post", "patch", "head", "options"]
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    paginate_by_param = "type_1"

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.query_params:
            filter_qs = {
                k: v for k, v in self.request.query_params.items() if k in VALID_PARAMS
            }
            qs = qs.filter(**filter_qs)
        return qs

    def post(self, request):
        serializer = PokemonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(f"{serializer.errors}", status=status.HTTP_400_BAD_REQUEST)


class PokemonDetailView(APIView):
    http_method_names = ["get", "patch", "head", "options"]
    serializer_class = PokemonSerializer

    def get(self, request, id):
        try:
            pokemon = Pokemon.objects.get(id=id)
        except Pokemon.DoesNotExist:
            return Response(
                f"Pokemon {id} does not exist", status=status.HTTP_404_NOT_FOUND
            )

        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data, status=status.HTTP_200_OK)
