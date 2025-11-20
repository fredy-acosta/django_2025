from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/', include('my_apps.category.urls')),
    path('api/product/', include('my_apps.product.urls')),
]