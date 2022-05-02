from django.urls import path

from CoffeeBusiness import settings
from mainpage import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing),
    path('about/', views.about),
    path('products/',views.products),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)