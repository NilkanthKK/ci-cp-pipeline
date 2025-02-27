from urllib import response
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
print('====================',secret_key)



# Create your views here.
@api_view(['GET'])
def ProductListCreate(request):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    return response({'data': 'succsess'})