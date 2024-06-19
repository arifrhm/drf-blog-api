from django.urls import path
from cms_app import views

urlpatterns = [
    path("api/posts/", views.PostListCreateAPIView.as_view(),
         name="post-list-create"),
    path("api/posts/<int:pk>/", views.PostDetailAPIView.as_view(),
         name="post-detail"),
    path(
        "api/posts/<int:pk>/update/",
        views.PostUpdateAPIView.as_view(),
        name="post-update",
    ),
    path(
        "api/posts/<int:pk>/delete/",
        views.PostDeleteAPIView.as_view(),
        name="post-delete",
    ),
    path(
        "api/images/", views.ImageListCreateAPIView.as_view(),
        name="image-list-create"
    ),
    path(
        "api/images/<int:pk>/", views.ImageDetailAPIView.as_view(),
        name="image-detail"
    ),
]
