from django.urls import path
# import views .. เมื่อ client เข้า url จะเรียก views.py
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), # เป็นการเรียกแบบ class base ของ django
]