from django.urls import path

from .views import HomePageview, CreatePostview

urlpatterns = [
    path('', HomePageview.as_view(), name='home'),
    path('post', CreatePostview.as_view(), name ='add_post'),

]