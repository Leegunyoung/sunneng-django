from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.
def hello(request):
    return render(request, "hello.html")

def home(request):
    blogs = Blog.objects

    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, "home.html" ,{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = Blog.objects.get(id=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def Aboutme(request):
    return render(request, 'Aboutme.html')

def create(request):
    blog=Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def delete(request, blog_id):
    Blog.objects.get(id=blog_id).delete()
    return redirect('/')

def edit(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'edit.html', {'blog':blog})

def update(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.title = request.POST.get('title')
    blog.body = request.POST.get('body')
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))





