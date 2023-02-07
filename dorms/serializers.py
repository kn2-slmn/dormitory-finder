from rest_framework.serializers import ModelSerializer
from .models import Dormitory

class DormitorySerializer(ModelSerializer):
    class Meta:
        model = Dormitory
        fields = '__all__'