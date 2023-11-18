"""
URL configuration for vonatinfo_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from vonatinfo_web import views

urlpatterns = [
    path('', views.train_list, name="train_list"),
    path('trains/<str:train_id>', views.train_detail, name="train_detail"),
    path('stations', views.station_list, name="station_list"),
    path('stations/<str:station_name>', views.station_detail, name="station_detail"),
]