from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, RegisterForm, CommentForm, UserProfileForm
from .models import Post, Comment, UserProfile

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
def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    comment.delete()
    return redirect('post_details', id=comment.post_id)


@login_required(login_url='/login')
def view_userprofile(request, id):
    userprofile = UserProfile.objects.filter(
        author_id=id).first()
    return render(request, 'main/view-userprofile.html', {'userprofile': userprofile})


@login_required(login_url='/login')
def create_userprofile(request):
    is_profile_exists = UserProfile.objects.filter(
        author_id=request.user.id).first()
    if is_profile_exists:
        messages.info(
            request, 'You already created your profile,/ now you can edit it, but you can\'t create anothor one')
        return redirect('/index')

    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.author = request.user
            profile.save()
            return redirect("/index")
    else:
        form = UserProfileForm()
    return render(request, 'main/create-userprofile.html',
                  {
                      'form': form,
                      'is_profile_exists': is_profile_exists
                  })


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
        post_detail = Post.objects.get(id=id)
    except post_detail.DoesNotExist():
        raise Http404(f"post with the id ({id}) is Not Found")
    if post_detail:
        comments = post_detail.comments.all().order_by('-created_at')
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.post = post_detail
                comment.save()
                return redirect(f'/post_detail/{id}')
        else:
            form = CommentForm()
        context = {
            'post_detail': post_detail,
            'comments': comments,
            'form': form,
        }
    return render(request, 'main/post_details.html', context)


@login_required(login_url='/login')
def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid:
        post = form.save(commit=False)
        post.save()
        messages.success(request, "You successfully updated the post")
        # return redirect('/index')
    else:
        messages.error(
            'The form was not updated successfully. Please enter in a title and content')
        form = PostForm()

    return render(request, "main/edit-page.html", {'form': form})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'new comment is added successfuly')
            return redirect('/index')
        else:
            messages.error(request, "invalid form")
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
