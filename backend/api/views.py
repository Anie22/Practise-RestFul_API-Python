# from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
@api_view(["POST"])
def api_home (request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        # data = model_to_dict(model_data, fields= ['title', 'content', 'price'] ) 
        return Response(serializer.data)
    return Response({"invalid": "not a good data"}, status=400)