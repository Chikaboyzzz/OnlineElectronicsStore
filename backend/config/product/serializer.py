from rest_framework import serializers

from .models import Product, Discount


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    discounts = DiscountSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
