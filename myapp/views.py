from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Maintenance
from .serializer import MaintenanceSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError

# Create your views here.
def Home(request):
    return HttpResponse('<h1>Hello world</h1')

def APIExample(request):
    data = {'message':'Hello World'}
    return JsonResponse(data=data)

@api_view(["GET"])  #มาจาก Decorator
@authentication_classes([])
@permission_classes([])
def MaintenanceAPI(request):

    try:
        maintenances = Maintenance.objects.all()
        serializer = MaintenanceSerializer(maintenances, many=True)
        return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    except Maintenance.DoesNotExist:
        return JsonResponse({"error":"ไม่พบข้อมูล"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def MaintenancePostAPI(request):
    if request.method == "POST":
        serializer = MaintenanceSerializer(data = request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"error":"มีข้อผิดพลาดเกิดขึ้น"}, status=status.HTTP_400_BAD_REQUEST)
