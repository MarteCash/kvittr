from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def bird_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            context['login_failed'] = True
    return render(request, 'birds/login.html', context)

def bird_logout(request):
    logout(request)
    return redirect('frontpage')

def bird_register(request):
    context = {}
    if request.method == "POST":
        if User.objects.filter(username=request.POST.get('username')):
            context['user_exists'] = True
            return render(request, 'birds/register.html', context)
        else:
            user = User()
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.username = request.POST.get('username').lower();
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password'))
            user.save()
            context['user_saved_successfully'] = True
    return render(request, 'birds/register.html', context)

@login_required
def bird_profile(request):
    context = {}
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        user.save()
        context['user_saved_successfully'] = True
    return render(request, 'birds/profile.html', context)