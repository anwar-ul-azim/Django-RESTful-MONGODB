from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('product', views.ProductView)
router.register('seller', views.SellerView)
router.register('subcategory', views.SubCategoryView)
router.register('category', views.CategoryView)
router.register('Customer', views.CustomerView)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
