from django.core.validators import MinValueValidator
from django.db import models, transaction
from decimal import Decimal
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos/', default='photos/default.jpg')

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='details')
    color = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        with transaction.atomic():
            # Уменьшение количества товара в модели Stocks
            try:
                stocks = Stocks.objects.select_for_update().get(productID=self.product)
                if stocks.qty < self.qty:
                    raise ValidationError('Insufficient stock quantity.')
                stocks.qty -= self.qty
                stocks.save()
            except Stocks.DoesNotExist:
                raise ValidationError('Product stock not found.')

            # Вычисление цены продукта и платы за доставку
            product_details = self.product.details
            delivery_fee = Decimal('0.05') * product_details.price  # 5% от цены продукта

            self.price = product_details.price + delivery_fee
            super().save(*args, **kwargs)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date_in_system = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class EmployeeInfo(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='info')
    marital_status = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate the discount price based on the product price and discount amount
        if self.product and self.amount:
            self.discount_price = self.product.details.price - (self.product.details.price * (self.amount / 100))

        # Check if this is an update to an existing discount
        if self.pk:
            super().save(*args, **kwargs)
        else:
            # Check if the product already has a discount associated with it
            existing_discount = Discount.objects.filter(product=self.product).first()
            if existing_discount:
                raise ValidationError('This product already has a discount associated with it.')
            else:
                super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.amount}% Discount"


class Stocks(models.Model):
    productID = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stocks')
    qty = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.productID} - Qty: {self.qty}"

