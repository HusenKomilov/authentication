from requests import Response
from rest_framework import generics, status
from users import models, serializers


class RegisterPhoneNumber(generics.GenericAPIView):
    serializer_class = serializers.UserPhoneRegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"data": "user_create"}, status=status.HTTP_201_CREATED)
