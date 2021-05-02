from django.urls import path

from django.conf.urls import url

from . import views
# For class based views
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    UserPostListView,
                    AnalyticsView, filter_posts)

urlpatterns = [
  path('', PostListView.as_view(), name = "blog-home"),
  path('about/', views.about, name = "blog-about"),
  path('post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
  path('post/new/', PostCreateView.as_view(), name = "post-create"),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name = "post-update"),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post-delete"),
  # path('user/<str:username>/', UserPostListView.as_view(), name = "user-posts"),
  url(r'^user/(?P<username>\w{0,50})/$', UserPostListView.as_view(), name='user-posts'),
  path('filter/', views.filter_posts, name = "filter"),
  path('analytics/', AnalyticsView.as_view(), name = "analytics"),
]



# TemplateDoesNotExist at blog/post_list.html
# <app>/<model>_<viewtype>.html