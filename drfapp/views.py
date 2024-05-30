from .models import Users
from .serializers import UserSerializer
from rest_framework import viewsets


class UserViewsets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer