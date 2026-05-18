from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


def index(request):
    return render(request, 'index.html')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer