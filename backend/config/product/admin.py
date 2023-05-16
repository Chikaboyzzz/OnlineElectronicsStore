from django.contrib import admin

from .models import Product, Category, ProductDetails, Order, OrderDetails, Customer, Employee, EmployeeInfo, Discount, Stocks

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductDetails)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(EmployeeInfo)
admin.site.register(Discount)
admin.site.register(Stocks)


