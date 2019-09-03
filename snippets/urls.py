
from django.conf.urls import url

from . import views
app_name = 'snippet'

urlpatterns = [
    url('hello/',  views.hello),    
]
