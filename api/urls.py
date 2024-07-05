from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path("blogposts/", BlogPostListAPIView.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>/", BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path(
        "updateCount/",
        increment_visitor_count,
        name="increment_visitor_count",
    ),
    path("getCount/", get_visitor_count, name="get_visitor_count"),
]
