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
        #Checks if the user exists in database
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
        new_username = request.POST.get('username').lower()
        #Checks if the username already exists
        if User.objects.filter(username=new_username).exists():
            context['user_exists'] = True
            return render(request, 'birds/register.html', context)          
        new_email = request.POST.get('email')
        #Checks if the email already exists
        if User.objects.filter(email=new_email).exists():
            context['email_exists'] = True
            return render(request, 'birds/register.html', context)
        #Creates new user
        user = User()
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.username = new_username
        user.email = new_email
        user.set_password(request.POST.get('password'))
        user.save()
        context['user_saved_successfully'] = True
    return render(request, 'birds/register.html', context)

@login_required
def bird_profile(request):
    context = {}
    if request.method == "POST":
        #Retrieves the user's (who's logged in) firstname, lastname and email
        user = request.user
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('email')
        #Saves changes
        user.save()
        context['user_saved_successfully'] = True
    return render(request, 'birds/profile.html', context)