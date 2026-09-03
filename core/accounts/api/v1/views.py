from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import RegistrationSerializer

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        ser_data = RegistrationSerializer(data = request.data)
        # ser_data.is_valid(raise_exception=True)
        if ser_data.is_valid():
            ser_data.save()
            data = {
                'email': ser_data.validated_data['email']
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)