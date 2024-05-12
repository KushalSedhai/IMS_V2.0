from rest_framework.serializers import ModelSerializer
from .models import User, ResourceType, Department, Resource, Vendor, Purchase

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class ResourceTypeSerializer(ModelSerializer):
    class Meta:
        model = ResourceType
        fields = '__all__'
        
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class VendorSerilizer(ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'