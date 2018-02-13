from rest_framework import serializers
from .models import Stock,Subcategory,Sku,Subcategory_SKU
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'
class SkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sku
        fields = '__all__'
class SubSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory_SKU
        fields = '__all__'