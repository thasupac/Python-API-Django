from django.urls import path, include
from .views import Home, APIExample, MaintenanceAPI, MaintenancePostAPI

urlpatterns = [
    path('', Home),  #รับมาจาก urls.py ของ mywebsite และส่งต่อไปยัง views.py ของ myapp
    path('api', APIExample),
    path('api/all-maintenance', MaintenanceAPI),
    path('api/post-maintenance', MaintenancePostAPI)
]