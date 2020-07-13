from .models import Profile 
from blog.models import Post 
from .forms import CreateUserForm , UserForm , ProfileForm 
from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordChangeForm
from allauth.socialaccount.models import SocialAccount

# Create your views here.

def profile(request,slug):
    profile = get_object_or_404(Profile , slug=slug)
    posts = Post.objects.all()
    context = {
        'profile':profile,
        'posts':posts,
    }
    return render(request , 'accounts/profile.html',context)

def register(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        else:
            form = CreateUserForm()
    context = {
        'form': form,
        'title':'register'
        }
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
                # Redirect to a success page.
    context = {
        'title':'login',
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


def passwordchange_view(request,slug):
    profile = get_object_or_404(Profile , slug=slug)
    socialaccount = SocialAccount.objects.filter(user=request.user) #to check if the user is in the social accounts list
    form = PasswordChangeForm(user=profile.user)

    if profile.user == request.user: #if the user isn't the profile's owner he can't change the password and he'll be redirected to the profile page
        if not socialaccount : #check if user use django allauth to login
            if request.method == 'POST':
                form = PasswordChangeForm(user=request.user, data=request.POST)
                if form.is_valid():
                    password = request.POST['new_password1'] 
                    form.save()
                    user = authenticate(request, username=profile.user.username, password=password)
                    login(request, user)
                    return redirect('/accounts/profile/%s'%profile.slug)
            else:
                form = PasswordChangeForm(user=profile.user)

        else:
            return redirect('/accounts/profile/%s'%profile.slug)        

    else:
        return redirect('/accounts/profile/%s'%profile.slug)


    context={
        'form':form,
        'title':'password change',
    }
    return render(request , 'accounts/changepassword.html',context)


def edit_profile(request , slug):
    userform = UserForm()
    profileform = ProfileForm()
    profile = get_object_or_404(Profile , slug=slug)

    if request.user == profile.user:
        if request.method == 'POST':
            userform = UserForm(request.POST , instance = request.user)
            profileform = ProfileForm(request.POST , request.FILES , instance = profile)
            if userform.is_valid and profileform.is_valid:
                userform.save()
                profileform.save()
                return redirect('/accounts/profile/%s'%profile.slug)
        else:
            userform = UserForm(instance = request.user)
            profileform = ProfileForm(instance = profile)
    else:
        redirect('/')
    context = {
        'userform':userform,
        'profileform':profileform,
        'title':'edit profile',
    }
    return render(request , 'accounts/edit.html', context)

def test(request, slug):
    account = get_object_or_404(Profile , slug=slug)
    social = SocialAccount.objects.all()
    if True:
        print(SocialAccount.objects.get(user=request.user))
    return render(request, 'accounts/test.html')