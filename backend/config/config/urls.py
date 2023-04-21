from django.contrib import admin
from django.urls import path
from product.views import ProductAPIList, ProductAPIUpdate, ProductAPIDestroy

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from product.views import DiscountAPIList, DiscountAPIUpdate, DiscountAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/product/', ProductAPIList.as_view()),
    path('api/v1/product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/v1/productdelete/<int:pk>/', ProductAPIDestroy.as_view()),

    path('api/v1/discount/', DiscountAPIList.as_view()),
    path('api/v1/discount/update/<int:pk>/', DiscountAPIUpdate.as_view()),
    path('api/v1/discount/delete/<int:pk>/', DiscountAPIDestroy.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
