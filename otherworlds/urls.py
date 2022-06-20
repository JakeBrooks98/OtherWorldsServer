"""app_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from otherworldsapi.views import register_user, login_user
from rest_framework import routers
from otherworldsapi.views.events import EventView
from otherworldsapi.views.worlds import WorldView
from otherworldsapi.views.biomes import BiomeView
from otherworldsapi.views.regions import RegionView
from otherworldsapi.views.maps import MapView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'worlds', WorldView, 'world')
router.register(r'events', EventView, 'event')
router.register(r'regions', RegionView, 'region')
router.register(r'biomes', BiomeView, 'biome')
router.register(r'maps', MapView, 'map')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]
