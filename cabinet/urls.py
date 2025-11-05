from django.urls import path
from .views import my_cabinet

urlpatterns = [
    path('my-cabinet/', my_cabinet, name='my_cabinet'),
]