from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.read_item, name='item_list'), 
    path('items/create/', views.create_item, name='create_item'),  
    path('items/<int:pk>/update/', views.update_item, name='update_item'),  
    path('items/<int:pk>/delete/', views.delete_item, name='delete_item'),  
]
