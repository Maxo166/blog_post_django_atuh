from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import PostForm, RegisterForm
from .models import Post

# Create your views here.


@login_required(login_url="/login")
def index(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get('post-id')
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, 'main/index.html', {'posts': posts})


@login_required(login_url='/login')
def create_post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('/index')
    else:
        form = PostForm()
    return render(request, 'main/create-post.html', {'form': form})


@login_required(login_url='/login')
def post_details(request, id):
    try:
        post_detail = Post.objects.get(pk=id)
    except post_detail.DoesNotExist:
        raise Http404(f"post with the id ({id}) is Not Found")
    return render(request, 'main/post_details.html', {'post_detail': post_detail})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/index')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
