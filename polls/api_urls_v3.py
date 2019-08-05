from django.conf.urls import url
from polls.views import pollAPIView

urlpatterns = [
    url('polls/', pollAPIView.as_view(), name="poll list API"),
]
