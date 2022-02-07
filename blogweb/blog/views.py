from aiohttp import request
from django.shortcuts import render
from .serializers import CatSerializer, BlogSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets
from .models import category, blog



# Create your views here.
def index(request):
    return render(request, 'index.html')

    

class blogview(ListAPIView):
    queryset= blog.objects.all()
    serializer_blog= BlogSerializer

class catlistview(ListAPIView):
    queryset= category.objects.all()
    serializer_blog= CatSerializer