from django.urls import path
from blogging.views import BlogListView, BlogDetailView, BlogAddPostView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("add", BlogAddPostView.as_view(), name="add_post"),
]
