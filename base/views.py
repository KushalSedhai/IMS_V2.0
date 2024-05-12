from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from .serilizer import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from .models import ResourceType, Resource, Department, Purchase, Vendor
from .serilizer import ResourceTypeSerializer, ResourceSerializer, VendorSerilizer, DepartmentSerializer, PurchaseSerializer
# Create your views here.


# USER Login system code start===========================================================================================================
# Registering the new user--------------------------------------------

@api_view(['POST',])
def register(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    request.data['password'] = hash_password
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User is Created")
    else:
        return Response(serializer.errors)

# User Login code-----------------------------------------------------------------------------

@api_view(['POST',])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username = email, password = password)
    
    if user == None:
        return Response("Incorrect Email or Password", status= status.HTTP_400_BAD_REQUEST)
    
    else:
        token,_ = Token.objects.get_or_create(user = user)
        return Response(token.key)
    

#   User based system code end==========================================================================
    

class ResourceTypeView(GenericAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ResourceTypeDetailView(GenericAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    
    def get(self, request,pk):
        try:
            queryset = ResourceType.objects.get(id=pk)
        except:
            return Response("no Data found", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            queryset = ResourceType.objects.get(id=pk)
        except:
            return Response("no Data found", status=status.HTTP_404_NOT_FOUND)
        
        serializer = ResourceTypeSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            queryset = ResourceType.objects.get(id=pk)
        except:
            return Response("no Data found", status=status.HTTP_404_NOT_FOUND)
        
        queryset.delete()
        return Response("Data is deleted")
    
 # =====================================================================================
    
class DepartmentView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
        
class ResourceView(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filterset_fields = ['typ', 'department']
    
class VendorView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerilizer

class PurchaseView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer