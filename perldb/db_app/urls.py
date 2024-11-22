from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    # path('<int:post_id>', views.blog_detail, name='blog_detail'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),

]

exit()

python manage.py shell


from thurModels.models import Student

student = Student.objects.create(
    first_name="john",
    last_name="Doe",
    email="john@example.com",
    phone="12229234"
)

alternative use this 

student = Student(
    first_name="john",
    last_name="Doe",
    email="john@example.com",
    phone="12229234"
)
student.save()