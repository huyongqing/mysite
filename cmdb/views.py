from django.shortcuts import render
from cmdb import models
from django.shortcuts import  HttpResponse
import json
from cmdb.models import UserInfo
# Create your views here.

# user_list = [
#     {"user":"jack","pwd":"abc"},
#     {"user":"tom","pwd":"ABC"}
# ]
#
#
# def index(request):
#     #return HttpResponse("helllo world!")
#     if request.method =="POST":
#         username = request.POST.get("username",None)
#         password = request.POST.get("password", None)
#         #添加数据到数据库
#         models.UserInfo.objects.create(user=username,pwd=password)
#     #从数据库读取全部数据
#     user_list = models.UserInfo.objects.all()
#         #temp = {"user": username, "pwd": password}
#         #user_list.append(temp)
#
#     return render(request,"login.html",{"data":user_list})

def login(request):
    return render(request,"login.html");
    # if request.method=="POST":
    #     name = request.POST.get("name",None)
    #     password = request.POST.get("password",None)
    #     #添加数据到数据库
    #     models.UserInfo.objects.create(name=name,pwd=password)
    #     if name=="yongqing.hu" and password=="HYq23931582!":
    #         return render(request,"login.html")
def switch(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        password = request.POST.get("password",None)

        if UserInfo.objects.filter(name=name,pwd=password):
            data = {'result': True}
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            return render(request,"login.html")


def index(request):
    return render(request,"index.html")

