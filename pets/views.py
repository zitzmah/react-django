from .models import Turtle
from rest_framework import viewsets, permissions
from .serializers import TurtleSerializer

class TurtleViewSet(viewsets.ModelViewSet):
    queryset=Turtle.objects.all()
    serializer_class=TurtleSerializer
    permission_classes=[permissions.AllowAny]