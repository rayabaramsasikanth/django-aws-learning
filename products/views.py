from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
class ProductListCreateView(generics.ListCreateAPIView):

    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer