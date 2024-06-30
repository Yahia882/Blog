from django.shortcuts import render
from datetime import date
from .models import Author, post_model, Tag, comment_section
from django.views.generic.base import View
from .form import comment_form
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse

def all_posts(request):
    posts = post_model.objects.all()
    return render(request, "all_posts.html", {
        "posts": posts
    })


def blog(request):

    sorted_posts = post_model.objects.order_by("-date")[:3]

    return render(request, "blog.html", {
        "posts": sorted_posts
    })


"""def Post (request,slug):
    # post = next(post for post in posts if post["post_title"]==slug)
     post_d =post.objects.get(slug =slug)
     all_tags = post_d.tags.all()
     return render(request,"post.html",{
        "post":post_d,
        "tags":all_tags
    })"""


class post_view(View):
    def get(self, request, **kwargs):

        post_d = post_model.objects.get(slug=kwargs["slug"])
        all_tags = post_d.tags.all()
        form = comment_form()
        comments_post = comment_section.objects.filter(Post=post_d.id)
        post__id = post_d.id
        if 'read_later' not in request.session:
         request.session["read_later"] = []
        rl = request.session.get("read_later")
        
        if post__id in rl:
           print("true")
           read_later = True
        else:
           print(rl)
           print(post__id)
           read_later = False

        
        return render(request, "post.html", {
            "post": post_d,
            "tags": all_tags,
            "form": form,
            "post_comment": comments_post,
            "red":read_later
        }) 

    def post(self, request, **kwargs):
        post_d = post_model.objects.get(slug=kwargs["slug"])
        all_tags = post_d.tags.all()
        
        form = comment_form(request.POST)
        new_form = form.save(commit=False)
        new_form.Post = post_d
        if form.is_valid():
         """new_form = form.save(commit=False)
         new_form.Post = post_d.id"""
         new_form.save()
        #x.save()
         return HttpResponseRedirect(reverse("post", args=[kwargs["slug"]]))
         
        else:
         comments_post = comment_section.objects.filter(Post=post_d.id)
         return render(request, "post.html", {
            "post": post_d,
            "tags": all_tags,
            "form": form,
            "post_comment": comments_post
        })


class read_later_posts(View):
   
   def post(self,request):
      if 'read_later' not in request.session:
       request.session["read_later"] = []
      
      id_post=int(request.POST["post_id"])
      list_id =request.session["read_later"]
      
      if  id_post not in  list_id:
         list_id.append(id_post)
      else:
         list_id.remove(id_post)
    
      post_d = post_model.objects.get(id=id_post)
      request.session["read_later"] = list_id
      
      return HttpResponseRedirect(reverse("post", args=[post_d.slug]))
   
   def get(self,request):
      if 'read_later' not in request.session:
       request.session["read_later"] = []
      x = request.session.get("read_later")
      post_later = post_model.objects.filter(id__in=x)
      return render(request,"read_later.html",{
         "posts":post_later,
         "empty": True if len(x)==0 else False
      })
