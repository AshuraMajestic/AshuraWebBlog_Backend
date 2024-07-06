from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path("blogposts/", BlogPostListAPIView.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>/", BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
]
