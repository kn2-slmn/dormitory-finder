from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.decorators import action

from accounts.models import User
from .models import Dormitory
from .serializers import DormitorySerializer

# Create your views here.

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method != 'POST' or \
            (request.user.is_authenticated and request.user.type == User.Types.OWNER)

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.owner.account == request.user


class DormitoryViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Dormitory.objects.all()
    serializer_class = DormitorySerializer

    @action(detail=False, methods=['GET'])
    def own_dormitory(self, request, pk=None):
        dorms = Dormitory.objects.filter(owner__account=request.user)
        serializer = self.get_serializer(dorms, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'])
    def search(self, request):
        search = request.GET.get('search')

        if search == None:
            search = ''

        dorms = Dormitory.objects.filter(name__icontains=search)
        serializer = self.get_serializer(dorms, many=True)
        return Response(serializer.data)