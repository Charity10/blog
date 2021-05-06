from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

def blogHome(request):
    context = {}
    return render(request, 'blog/home.html', context)

class BlogDetailView(DetailView):
    model = Post
    template_name = 'about/post_detail.html'

class BlogCreateView(CreateView): 
    model = Post    
    template_name = 'postNew/post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'edit/post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete/post_delete.html'
    success_url = reverse_lazy('home')
