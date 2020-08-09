from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
  return HttpResponse("<em>My Second App</em>")

def help(request):
  context_dictionary = {
    'help_content': "Here's a bunch of help content yo"
  }
  return render(request, 'AppTwo/help.html', context=context_dictionary)
