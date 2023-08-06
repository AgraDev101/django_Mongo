from rest_framework import serializers
from .models import Product, Category, Cart, User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['_id', 'title', 'description' ,'price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['_id', 'name']