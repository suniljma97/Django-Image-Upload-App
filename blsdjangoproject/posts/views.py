# from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post

class HomePageview(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostview(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')