from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from tools.models import Tool
from users.models import Profile

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
    notools = Tool.objects.count()
    noprofiles = Profile.objects.count()

    details = {'home': 'w3-blue'}
    details['notools'] = notools
    details['noprofiles'] = noprofiles
    return render(request, 'controlpanel/home.html', {'details': details})

@login_required
def controlpanel_tools(request):
    tools = Tool.objects.all()
    details = {'tools': 'w3-blue'}
    return render(request, 'controlpanel/tools.html', {'details': details, 'tools': tools})

@login_required
def controlpanel_logout(request):
    logout(request)
    return redirect('controlpanel_login')
