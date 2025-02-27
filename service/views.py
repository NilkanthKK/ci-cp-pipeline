from urllib import response
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def ProductListCreate(request):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    return response({'data': 'succsess'})