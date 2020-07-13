from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Profile
from .models import Post , Comment
from .forms import CreatePostForm , CommentForm , EmailForm


# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-creation_date')
    context = {
        'posts':posts
        }
    return render(request, "blog/index.html", context)

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        comment_text = request.POST['comment']
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            if len(comment_text)>0:
                comment = Comment.objects.create(post=post, profile=profile, text=comment_text)
                comment.save()    
                return redirect('/post/%s'% slug)
        else:
            return redirect('/accounts/login/')
    context = {
        'post':post,
    }
    return render(request, 'blog/post.html', context)


@login_required(redirect_field_name='/accounts/login/')
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid:
            newform = form.save(commit=False)
            newform.profile = Profile.objects.get(user=request.user)
            newform.save()
            return redirect('/')
    else:
        form = CreatePostForm()
            
    context = {
        'form':form,
        'title':'create post',
    }
    return render(request , 'blog/create.html', context)

def edit(request, slug):
    post=get_object_or_404(Post, slug=slug)
    if request.user == post.profile.user:
        if request.method == 'POST':
            form = CreatePostForm(request.POST, instance=post)
            if form.is_valid:
                newform = form.save(commit=False)
                newform.profile = Profile.objects.get(user=request.user)
                newform.save()
                return redirect('/post/%s' % slug)
        else:
            form = CreatePostForm(instance=post)
    else:
        return redirect('/post/%s' % slug)
    context = {
        'form':form,
        'title':'edit %s'%post.slug,
    }
    return render(request, 'blog/edit.html', context)

@login_required(redirect_field_name='/accounts/login/')
def user_posts(request, slug):
    profile = Profile.objects.get(slug=slug)
    posts = Post.objects.filter(profile=profile)
    context = {
        'posts':posts,
        'title':'%s posts'%profile.slug,
    }
    return render(request, 'blog/your_blog.html', context)

def delete(request, slug):
    post=Post.objects.get(slug=slug)
    if request.user == post.profile.user:
        post.delete()
        return redirect('/')
    else:
        return redirect('/')


# def add_comment_to_post(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     profile = Profile.objects.get(user=request.user)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if request.user.is_authenticated:
#             if form.is_valid():
#                 comment = form.save(commit=False)
#                 comment.post = post
#                 comment.profile = profile
#                 comment.save()
#                 return redirect('/post/%s'% slug)
#         else:
#             return redirect('/accounts/login/')        
#     else:
#         form = CommentForm()
#     context = {
#         'form': form
#         }
#     return render(request, 'blog/add_comment_to_post.html', context)





# def test(request):
#     return render(request, 'blog/test.html')

