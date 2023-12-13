from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/", views.about, name="about"),
    path("services/", views.service, name="services"),
    path("services/car-insurance", views.car_insurance, name="car_insurance"),
    path("services/life-insurance", views.life_insurance, name="life_insurance"),
    path("services/health-insurance", views.health_insurance, name="health_insurance"),
    path("services/home-insurance", views.home_insurance, name="home_insurance"),
]
