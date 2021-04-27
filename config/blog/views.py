from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

#def blogHome(request):
 #  context = {}
    #return render(request, 'blog/home.html', context)

class BlogDetailView(DetailView):
    model = Post
    template_name = 'about/post_detail.html'