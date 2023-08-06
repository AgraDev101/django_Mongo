from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category, User, Cart
from rest_framework.generics import ListAPIView

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# Create your views here.
