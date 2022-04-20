from django.urls import path
from mainpage import views

urlpatterns = [
    path('', views.landing),
    path('about/', views.about),
    path('products/',views.products),
]