from django.urls import path, include
from .views import ListCategory, DetailCategory, ListBook, DetailBook, ListProduct, DetailProduct, UserViewSet
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'carts', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='singlecategory'),
    path('books', ListBook.as_view(), name='books'),
    path('books/<int:pk>/', DetailBook.as_view(), name='singlebook'),
    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
    path('auth/', obtain_auth_token),
    path('carts/', ListCart.as_view(), name='allcarts'),
    path('carts/<int:pk>', DetailCart.as_view(), name='cartdetail'),

]


