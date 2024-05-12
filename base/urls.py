from django.urls import path
from .views import register, login, ResourceTypeView, ResourceTypeDetailView, DepartmentView, ResourceView, VendorView, PurchaseView

urlpatterns = [
    path('register/', register ),
    path('login/', login ),
    path('resourcetype/', ResourceTypeView.as_view()),
    path('resourcetype/<int:pk>/', ResourceTypeDetailView.as_view()),
    
    path('department/', DepartmentView.as_view({'get':'list', 'post':'create'})),
    path('department/<int:pk>/', DepartmentView.as_view({'get':'retrieve', 'put':'update','delete':'destroy'}) ),
    
    path('resource/', ResourceView.as_view({'get':'list', 'post':'create'})),
    path('resource/<int:pk>/', ResourceView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy' }) ),
    
    
    path('vendor/', VendorView.as_view({'get':'list', 'post':'create'})),
    path('vendor/<int:pk>/', VendorView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}) ),
    
    path('purchase/', PurchaseView.as_view({'get':'list', 'post':'create'}) ),
    path('purchase/', PurchaseView.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}) ),
    
]