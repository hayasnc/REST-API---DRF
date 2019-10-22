from django.conf.urls import url

from .views import HomePageView, CreatePostView
app_name = 'image_processor'

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url('post/', CreatePostView.as_view(), name='add_post') # new
]
