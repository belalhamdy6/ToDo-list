from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='list'),
    path('update/<str:pk>', views.Update, name='update'),
    path('delete/<str:pk>', views.Delete, name='delete'),
]
