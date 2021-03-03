from django.urls import path

from .views import (
    blog_post_list_view,
    blog_post_detail_view,
blog_post_update_view,
blog_post_delete_view,
)

urlpatterns = [
    path('',blog_post_list_view, name='blogpost'),
    path('<slug:slug>/edit/', blog_post_update_view),
    path('<slug:slug>/delete/', blog_post_delete_view),
    path('<slug:slug>/', blog_post_detail_view),
]
