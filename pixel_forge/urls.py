from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_form, name='img'),
    path('process/', views.image_view, name='image_view'),
]