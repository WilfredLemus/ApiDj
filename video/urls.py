from django.conf.urls import url
from .views import ListVideo, DetailVideo

urlpatterns = [
    url(r'^videos/$', ListVideo.as_view(), name="list_video"),
    url(r'^videos/(?P<pk>[0-9]+)$', DetailVideo.as_view(), name="detail_video"),
]
