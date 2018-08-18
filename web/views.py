from django.shortcuts import render
from tools.models import Tool

def home(request):
    tools = list(Tool.objects.all().order_by('?'))[0:3]
    return render(request, 'web/home.html', {'tools': tools})

def tools(request):
    tools = Tool.objects.all()
    return render(request, 'web/tools.html', {'tools': tools})
