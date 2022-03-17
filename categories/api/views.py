from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from categories.models import Category
from categories.api.serializers import CategorySerializer


class CategoriesView(APIView):
    """
    Vista para ver las categorias y crearlas
    """
    def get(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)  # El many=True es para que devuelva el array
        # Completo de los posts
        if len(serializer.data) == 0:
            return Response(status=status.HTTP_200_OK, data={'message': 'There is no categories yet'})
        else:
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.POST)  # Con esto el serializador buscara los datos que debe buscar
        serializer.is_valid(raise_exception=True)  # Y con esto, si ocurre algun error o algun dato es invalido, elevara
        # Una excepcion
        serializer.save()  # Y este save para guardar en la base de datos
        return Response(status=status.HTTP_200_OK, data=serializer.data)
