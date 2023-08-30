from cgitb import lookup
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)  
product_list_create_view = ProductListCreateAPIView.as_view()   

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
       instance = serializer.save()
       if  not instance.content:
        instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()   

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance == True:
            super.perform_destroy(instance)

product_destroy_view = ProductDeleteAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()
 

@api_view(['GET', 'POST'])
def product_all_view(request,pk):
    # method = request.method

    if request.method == "GET":
        if Product.objects.filter(pk = pk).exists():
            product = Product.objects.get(pk = pk)
            data = ProductSerializer(product, many=False)
            return Response(data.data)
    #     queryset = Product.objects.all()
    #     data = ProductSerializer(queryset, many=True).data
    #     return Response(data)
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response(serializer.data)
    # return Response({"invalid": "not a good data"}, status=400)
