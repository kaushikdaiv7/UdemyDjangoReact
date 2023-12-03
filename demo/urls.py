from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet


router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('first', views.first),
    path('second', views.second),
    path('another', views.Another.as_view()),
    path('third', views.third),
    path('', include(router.urls))
]
