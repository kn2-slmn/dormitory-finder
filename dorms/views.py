from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .models import Dormitory
from .serializers import DormitorySerializer

# Create your views here.

class DormitoryViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer