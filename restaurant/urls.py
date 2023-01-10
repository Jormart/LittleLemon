from django.contrib import admin 
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    # path('booking/', views.BookingView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('about/', views.about, name='about'),
    
]