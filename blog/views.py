from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

def blog(request):
    v_post = Post.objects.all()
    return render(request, 'index.html', {"post":v_post})

def criarpost(request):
    return render(request, 'criarpost.html')


def create_Post(request):
    v_nome = request.POST.get("nome")
    v_categoria = request.POST.get("categoria")
    v_artigo =  request.POST.get("artigo")
    v_Post = Post.objects.all()
    Post.objects.create(nome=v_nome, categoria = v_categoria, artigo = v_artigo )
    return render(request, 'index.html', {"post":v_Post})

def blog_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog_post.html', {"post":post})