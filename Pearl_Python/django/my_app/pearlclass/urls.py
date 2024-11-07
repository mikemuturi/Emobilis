# pearlclass/urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
    path('about/', views.about, name='my_About'),
    path('services/', views.services, name='my_Services'),  # This should match the 'my_Services' pattern
    path('blog/', views.blog, name='my_Blog'),
    path('contact/', views.contact, name='my_Contact'),
]
