from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from tools.models import Tool
from users.models import Profile

from .forms import ToolEditForm, ToolNewForm

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

    newform = ToolNewForm()
    editform = ToolEditForm()
    return render(request, 'controlpanel/tools.html', {'details': details, 'tools': tools, 'editform': editform, 'newform': newform})

@login_required
def controlpanel_logout(request):
    logout(request)
    return redirect('controlpanel_login')

@login_required
def new_tools(request):
    if request.method == 'POST':        
        form = ToolNewForm(request.POST)        
        if form.is_valid():
            tool = Tool.objects.create(
                serialno = form.cleaned_data.get('serialno'),
                make = form.cleaned_data.get('make'),
                rentalvalue = form.cleaned_data.get('rentalvalue'),
                desc = form.cleaned_data.get('desc'),
            )
            return redirect('controlpanel_tools')

@login_required
def edit_tools(request):
    tool = Tool.objects.get(pk=request.GET.get('pk'))
    data = { 'pk':tool.pk, 'serialno':tool.serialno, 'make':tool.make, 'rentalvalue':tool.rentalvalue, 'desc':tool.desc }
    return JsonResponse(data, safe=False)

@login_required
def update_tools(request):
    print(request.POST.get('pk'))
    tool = Tool.objects.get(pk=request.POST.get('pk'))
    tool.serialno = request.POST.get('serialno')
    tool.make = request.POST.get('make')
    tool.rentalvalue = request.POST.get('rentalvalue')
    tool.desc = request.POST.get('desc')
    tool.save()
    
    return redirect('controlpanel_tools')

@login_required
def delete_tools(request):
    print(request.POST.get('pk'))
    Tool.objects.get(pk=request.POST.get('pk')).delete()
       
    return redirect('controlpanel_tools')

