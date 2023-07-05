
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('create/<id>/', views.create),
    path('read/', views.read),
    path('update/', views.update),
    path('delete/', views.delete)
]
