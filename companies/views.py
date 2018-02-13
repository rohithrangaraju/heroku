from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .models import Users
from django.http import HttpResponse
from .models import Subcategory,Sku,Subcategory_SKU
from .serializer import StockSerializer,SubcategorySerializer,SkuSerializer,SubSkuSerializer
from .library import mytokeng
# class StockList(APIView):
#     def get(self,request):
#         stocks = Stock.objects.all();
#         serializers = StockSerializer(stocks,many=True)
#         return Response(serializers.data)
#     def post(self):
#         pass
# class Authenticate(APIView):
#     def get(self,request,username,password):
#         response =''
#         try:
#             current_user = Users.objects.get(username=username,password=password)
#             tokenclass = mytokeng()
#             response = tokenclass.generate(username,password)
#
#         except Users.DoesNotExist:
#             response = 'Not Authenticated'
#         return Response(response)
class DisplayAllSubcategory(APIView):
    def get(self,request):
        try:
            sub_category_data = Subcategory.objects.all()
            serializers = SubcategorySerializer(sub_category_data,many=True)
            return Response(serializers.data)
        except:
            return Response('Not found')
class FetchSubcategoryDetails(APIView):
    def get(self,request,sub_category_id):
        try:
            sub_category = Subcategory.objects.get(sub_category_id = int(sub_category_id))
            serializers = SubcategorySerializer(sub_category, many=False)
            return Response(serializers.data)
        except:
            return Response('Not found')
class FetchAllSku(APIView):
    def get(self,request,sub_category_id):
        try:
            import json
            subcategoryData = Subcategory.objects.get(sub_category_id=sub_category_id)
            skuData = Subcategory_SKU.objects.values_list('sku_id', flat=True).filter(sub_category_id=subcategoryData)
            # print(skuData)
            skufullData = []
            for i in skuData:
                #print(type(i))
                data1 = Sku.objects.values_list('sku_description').get(sku_id=i)
                skufullData.append({'sku_id': i, 'sku_description': data1[0]})
            return HttpResponse(skufullData)
            # for i in a1:
            #     mainList.append({'sku_id':i['pk'],'sku_description':i['fields']['sku_description']})
        except :
            return Response('Not Found')
class FetchSkuDescription(APIView):
    def get(self,request,sub_category_id,sku_id):
        try:
            sku_data = Sku.objects.get(sku_id=int(sku_id))
            serializers = SkuSerializer(sku_data,many=False)
            return Response(serializers.data)
        except:
            return Response('Not found')