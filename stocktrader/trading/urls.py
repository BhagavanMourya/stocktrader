from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trade/', views.trade, name='trade'),
    path('history/', views.history, name='history'),
]