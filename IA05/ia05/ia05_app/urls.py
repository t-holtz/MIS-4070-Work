from django.urls import path
from ia05_app import views

urlpatterns = [
    path('', views.ia05_app, name='ia05_app'),
]
