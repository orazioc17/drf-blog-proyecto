from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.models import User
from users.api.serializers import PostSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.POST)  # Con esto el serializador buscara los datos que tiene q buscar
        serializer.is_valid(raise_exception=True)  # Y con esto, si ocurre algun error o algun dato es invalido, elevara
        # Una excepcion
        serializer.save()  # Y este save para guardar en la base de datos
        return Response(status=status.HTTP_200_OK, data=serializer.data)
