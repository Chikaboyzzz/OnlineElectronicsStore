from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discounts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate the discount price based on the product price and discount amount
        if self.product and self.amount:
            self.discount_price = self.product.price - (self.product.price * (self.amount / 100))

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
