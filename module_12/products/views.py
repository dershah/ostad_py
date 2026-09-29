from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductListSerializer, ProductDetailSerializer

class ProductListView(APIView):
    permission_classes = []  

    def get(self, request):
        products = Product.objects.all()

        serializer = ProductListSerializer(
            products, 
            many=True
        )

        data = serializer.data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = ProductListSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class ProductView(APIView):
    permission_classes = []  

    def get(self, request, pk):
        product = Product.objects.get(id=pk)

        serializer = ProductDetailSerializer(
            product
        )
        data = serializer.data

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        product = Product.objects.get(id=pk)

        serializer = ProductDetailSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_204_NO_CONTENT
            )
       
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def patch(self, request, pk):
        product = Product.objects.get(id=pk)

        serializer = ProductDetailSerializer(
            product,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_204_NO_CONTENT
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )