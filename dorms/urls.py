from django.urls import path

from .views import DormitoryViewSet

dormitory_list = DormitoryViewSet.as_view({
    'get' : 'search',
    'post' : 'create'
})
dormitory_detail = DormitoryViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})
own_dormitory = DormitoryViewSet.as_view({
    'get' : 'own_dormitory'
})
search_dormitory = DormitoryViewSet.as_view({
    'get' : 'search'
})

urlpatterns = [
    path('', dormitory_list),
    path('<int:pk>', dormitory_detail),
    path('my/', own_dormitory)
]