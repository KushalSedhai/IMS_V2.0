from django.contrib import admin
from .models import User, ResourceType, Department, Resource, Vendor, Purchase

# Register your models here.
admin.site.register(User)
admin.site.register(ResourceType)
admin.site.register(Department)
admin.site.register(Resource)
admin.site.register(Vendor)
admin.site.register(Purchase)
