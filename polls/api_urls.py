from django.conf.urls import url
from polls.views import poll, poll_details

urlpatterns = [
    url(r'^polls/(?P<nana_id>\d+)/$', poll_details),
    url('polls', poll),
]
