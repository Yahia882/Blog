from . import views
from django.urls import path

urlpatterns = [
    path("",views.blog,name="blog"),
    path("posts/",views.all_posts,name="all_posts"),
    path("posts/read_later/",views.read_later_posts.as_view(),name="read_later"),
    path("posts/<slug:slug>/",views.post_view.as_view(),name="post"),
    
]
