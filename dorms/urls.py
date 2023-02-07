from django.urls import path

from .views import DormitoryViewSet

dormitory_list = DormitoryViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})
dormitory_detail = DormitoryViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

urlpatterns = [
    path('', dormitory_list),
    path('<int:pk>', dormitory_detail)
]