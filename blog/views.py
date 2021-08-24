from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,HttpResponse,redirect
from django.db import IntegrityError,models
import random

from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def blogpost(request,slug):
    posts=Post.objects.filter(slug=slug)
    context={'Post': posts}
    # return HttpResponse(f"This is {slug}")
    return render(request,'blog/blogpost.html',context)

# class (CreateView):
#     model = Post
#     # the fields mentioned below become the entry rows in the generated form
#     fields = ['content']


def addblog(request):
    
    # if request.method=='POST':
    #     title=request.POST['title']

    #     if(len(title)<1):
    #         messages.error(request,"Please enter suitable title!")
    #     else:
    #         post=Post(title=title)
    #         post.save()
    if request.method=='POST':
        blog=request.POST['blog']
        if len(blog)<40:
            messages.error(request,"Please enter enough content and suitable title!")
            return redirect('./addblog')
        else:
            post=Post(content=blog,slug='blogpost'+str(Post.sno)) 
            post.save()
            messages.success(request,"Yay...your Blog has been published successfully!")
            return redirect('./')
#     # if request.method=='POST':
#     #     blog=request.POST['blog']
#     #     if len(title)<1 or len(content)<40:
#     #         messages.error(request,"Please enter enough content and suitable title!")
#     #         return redirect('/addblog')
#     #     else:
#     #         post=Post(title=title,content=blog)
#     #         post.save()
#     #         messages.success(request,"Yay...your Blog has been published successfully!")
#     #         return redirect('/bloghome')
    return render(request,'blog/addblog.html')



def bloghome(request): 
    
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request,'blog/bloghome.html',context)