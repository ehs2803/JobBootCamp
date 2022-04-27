from django.urls import path
from product import views

urlpatterns = [
    path('<int:content_id>/', views.detail),
]