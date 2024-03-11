"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from plants import views as plant
from flowers import views as flower
from gifts import views as gift

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',plant.index,name="home"),
    path('showPlant/',plant.showplant,name="showplant"),
    path('detailsplant/<int:id>/',plant.detailsplant,name="detailsplant"),
    path('auth_register/',plant.auth_register,name='auth_register'),
    path('auth_login/',plant.auth_login,name='auth_login'),
    path('auth_logout/',plant.auth_logout,name='auth_logout'),
    path("checkout/",plant.checkout, name="checkout"),
    path("success/",plant.success,name='success'),
    path('add_to_cart/<int:id>/',plant.add_to_cart,name='add_to_cart'),
    path('showCart/',plant.show_cart,name='showcart'),
    path('delete_cart/<int:id>/',plant.delete_cart,name='delete_cart'),
    path('showflower/',flower.showflower,name='showflower'),
    path('detailsflower/<int:id>/',flower.detailsflower,name='detailsflower'),
    path('add_to_cart_f/<int:id>/',flower.add_to_cart_f,name='add_to_cart_f'),
    path('showgift/',gift.showgift,name='showgift'),
    path('detailsgift/<int:id>/',gift.detailsgift,name='detailsgift'),
    path('add_to_cart_g/<int:id>/',gift.add_to_cart_g,name='add_to_cart_g')
]


