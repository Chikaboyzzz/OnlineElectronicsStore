from django.http import HttpResponse
from django.views import View
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import ProductSerializer, DiscountSerializer, ProductDetailsSerializer
from rest_framework import filters
from .models import Product, ProductDetails, Discount


class ProductAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']


class ImageView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        image_path = product.image.path
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')


class ProductDetailAPIList(generics.ListCreateAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer


class ProductAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class ProductAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DiscountAPIList(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


