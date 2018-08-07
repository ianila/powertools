from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login

def controlpanel_login(request, template_name='controlpanel/login.html'):
    username = request.POST.get('usename', False)
    password = request.POST.get('psw', False)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)            
            return redirect('controlpanel_home')
        else:
            return render(request, template_name, {'error': 'disabled account'})
    else:
        return render(request, template_name, {'error': 'invalid login'})
