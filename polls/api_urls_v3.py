from django.conf.urls import url
from polls.views import pollAPIView, UserViewSet, GroupViewSet

urlpatterns = [
    url('polls/questions', pollAPIView.as_view(), name="poll list API"),
    url('polls/auth/user', UserViewSet, name="User"),
    url('polls/auth/group', GroupViewSet, name="Group"),
]
