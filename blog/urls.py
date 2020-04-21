from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name="post_detail"),
    url(r'post_create/$', views.post_create, name="post_create"),
]
