from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def controlpanel_login(request, template_name='controlpanel/login.html'):
    if request.method == 'POST': 
        username = request.POST.get('usrname', False)
        password = request.POST.get('psw', False)
        user = authenticate(username=username, password=password)    
        if user is not None:
            if not user.profile.role == 'CUSTOMER':
                login(request, user)            
                return redirect('controlpanel_home')
            else:
                return render(request, template_name, {'error': 'you do not have permission to login'}) 
        else:
            return render(request, template_name, {'error': 'something went wrong. try again !'})            
    else:
        return render(request, template_name)

@login_required
def controlpanel_home(request):
    return render(request, 'controlpanel/home.html')
