from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import DepartmentSerializer
from .models import Cure

# Create your views here.


@api_view(['GET'])
def ViewMedicine(request, pk):
    product = Cure.objects.get(id=pk)
    serializer = DepartmentSerializer(product, many=False)
    return Response(serializer.data)
@api_view(['GET'])
def ShowAll(request):
    products = Cure.objects.all()
    serializer = DepartmentSerializer(products, many=True)
    return Response(serializer.data)
