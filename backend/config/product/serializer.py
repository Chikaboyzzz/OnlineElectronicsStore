from rest_framework import serializers
from django.utils import timezone

from .models import Product, Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()
    price_with_discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'discount', 'price_with_discount')

    def get_discount(self, obj):
        discounts = obj.discounts.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
        if discounts.exists():
            return "Yes"
        else:
            return "No"

    def get_price_with_discount(self, obj):
        discounts = obj.discounts.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
        if discounts.exists():
            discount = discounts.first()
            discounted_price = obj.price - (obj.price * (discount.amount / 100))
            return round(discounted_price, 2)
        else:
            return None
