from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:course_pk>/<int:step_pk>', views.step_detail, name='step_detail'),
]
