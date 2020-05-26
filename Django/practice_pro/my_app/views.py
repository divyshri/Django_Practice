from django.shortcuts import render

# Create your views here.
def index(request):
    my_dic = {'my_template':"Hello Divyanshu Here"}
    return render(request,'my_app/index.html',context=my_dic)
