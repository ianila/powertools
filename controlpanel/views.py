from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from tools.models import Tool
from users.models import Profile

from .forms import ToolEditForm

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

    editform = ToolEditForm()
    return render(request, 'controlpanel/tools.html', {'details': details, 'tools': tools, 'editform': editform})

@login_required
def controlpanel_logout(request):
    logout(request)
    return redirect('controlpanel_login')

@login_required
def edit_tools(request):
    tools = list(Tool.objects.values())
    return JsonResponse(tools, safe=False)

@login_required
def update_tools(request):
    tool = Tool.objects.get(serialno=request.POST.get('serialno'))
    tool.serialno = request.POST.get('serialno')
    tool.make = request.POST.get('make')
    tool.rentalvalue = request.POST.get('rentalvalue')
    tool.desc = request.POST.get('desc')
    tool.save()
    
    return redirect('controlpanel_tools')
