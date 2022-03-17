from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from users.api.serializers import UserRegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)  # Con esto el serializador buscara los datos que
        # tiene q buscar
        if serializer.is_valid(raise_exception=True):  # Y con esto, si ocurre algun error o algun dato es invalido,
            # elevara una excepcion
            serializer.save()  # Y este save para guardar en la base de datos
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
