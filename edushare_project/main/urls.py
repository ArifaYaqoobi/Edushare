from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('resource/<int:pk>/', views.resource_detail, name='resource_detail'),
    path('resource/add/', views.resource_add, name='resource_add'),
    path('api/search/', views.api_search, name='api_search'),
]
