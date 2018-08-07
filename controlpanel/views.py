from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def controlpanel_login(request, template_name='controlpanel/login.html'):
    username = request.POST.get('usrname', False)
    password = request.POST.get('psw', False)
    user = authenticate(username=username, password=password)    
    if user is not None:
        print(user.username)
        if user.is_active:
            login(request, user)            
            return redirect('controlpanel_home') #return render(request, 'controlpanel/home.html')
        else:
            print('disabled account')
            return render(request, template_name, {'error': 'disabled account'})            
    else:
        print('invalid login')
        return render(request, template_name, {'error': 'invalid login'})

@login_required
def controlpanel_home(request):
    return render(request, 'controlpanel/home.html')
