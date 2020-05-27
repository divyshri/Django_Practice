from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
# Create your views here.

def user(request):
    user_list = User.objects.order_by('first_name')
    data_dict = {'user_info':user_list}
    return render(request,'appTwo/user.html',context=data_dict)


def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)
