from django.contrib import admin
from django.urls import path
from product.views import ProductAPIList, ProductAPIUpdate, ProductAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', ProductAPIList.as_view()),
    path('api/v1/product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/v1/productdelete/<int:pk>/', ProductAPIDestroy.as_view()),
]
