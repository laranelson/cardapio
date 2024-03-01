from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'goMenu'

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include('products.urls')),
    path('menus/', include('menus.urls')),
    path('orders/', include('orders.urls')),
    path('', include('restaurants.urls')),
] 