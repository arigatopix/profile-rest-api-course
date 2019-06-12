from django.urls import path, include
# import views .. เมื่อ client เข้า url จะเรียก views.py
from profiles_api import views
# map logic handling incoming requests () [DefaultRouter : response containing hyperlinks to all the list views]
from rest_framework.routers import DefaultRouter

# DefaultRouter คือ เมื่อเข้า /api/ จะแสดงผล urls ที่ register ไว้ในหน้านี้ เพื่อดูว่ามี url อะไรบ้าง
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
""" ? access API Viewset (url ตั้งชื่อที่ base_name หรือใช้ queryset) """

# register UserProfileViewSet
router.register('profile', views.UserProfileViewSet)
""" ไม่ต้องมี basename เพราะ queryset provide ให้ """

urlpatterns = [
    # เป็นการเรียกแบบ class base ของ django
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),  # คือเข้า hello-viewset/
]
