from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,CreateView,DetailView,UpdateView,DeleteView)


# Create your views here.
'''def home(request):

    context={'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)'''

#List View demo
class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    template_name='blog/post_create.html'
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model=Post

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']
    template_name="blog/post_update.html"
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name="blog/post_delete.html"
    success_url="/"
    def test_func(self):
        post=self.get_object()
        if(self.request.user==post.author):
            return True
        return False




        