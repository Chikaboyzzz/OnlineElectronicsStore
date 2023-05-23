from rest_framework import serializers
from django.utils import timezone
from rest_framework import serializers
from .models import Category, Product, ProductDetails, Order, OrderDetails, Customer, Employee, EmployeeInfo, Discount, Stocks


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_discount(self, obj):
        discounts = obj.discounts.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
        if discounts.exists():
            return "Yes"
        else:
            return "No"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'

    def create(self, validated_data):
        order_details = super().create(validated_data)

        # Уменьшение количества товара в модели Stocks
        product = order_details.product
        qty = order_details.qty
        stocks = Stocks.objects.get(productID=product)

        if stocks.qty >= qty:
            stocks.qty -= qty
            stocks.save()
        else:
            raise serializers.ValidationError("Insufficient stock quantity.")

        return order_details


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = '__all__'

