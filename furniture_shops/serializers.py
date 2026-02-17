from rest_framework.serializers import ModelSerializer
from.models import Furniture

class FurnitureSerializer(ModelSerializer):
    class Meta:
        model = Furniture
        fields = "__all__"

