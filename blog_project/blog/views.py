from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth import logout


# -----------------------------
# HOME PAGE (all posts)
# -----------------------------
def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


# -----------------------------
# LIST OF POSTS
# -----------------------------
def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


# -----------------------------
# CREATE POST (Login Required)
# -----------------------------
@login_required
def post_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   
            post.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()

    return render(request, 'blog/post_form.html', {'form': form})


# -----------------------------
# UPDATE POST (Login Required)
# -----------------------------
@login_required
def post_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'post': post})


# -----------------------------
# DELETE POST (Login Required)
# -----------------------------
@login_required
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


# -----------------------------
# POST DETAILS
# -----------------------------
def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# -----------------------------
# USER SIGNUP
# -----------------------------
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('post_list')