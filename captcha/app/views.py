from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

class BaseView(View):
    def get(self,request):
        return render(request,'base.html')
    
class IndexView(TemplateView):
    template_name='index.html'
    def get(self, request, *args, **kwargs):
        context = {
            'body': "<iframe src='https://minelords.github.io' width='1000' height='600' ></iframe>"  # 将参数传递给模板
        }
        return render(request, self.template_name, context)
        
class LoginView(TemplateView):
    template_name='login.html'
    
    def post(self,request):
        #print(request.POST)
        data={}
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            data['status']=0
        else:
            data['status']=1
        return JsonResponse(data)
        
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))