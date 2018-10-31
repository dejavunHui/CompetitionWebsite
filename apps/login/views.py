from django.shortcuts import render
from django.views import View
from .forms import CheckLoginForm
from ..user.models import User
# Create your views here.


class LoginView(View):
	'''
	用户登录在此处处理
	'''

	def get(self,request,*args,**kwargs):
		'''
		get请求
		'''
		return render(request,'login/login.html',{'user':CheckLoginForm()})

	def post(self,request,*args,**kwargs):
		'''
		post请求
		'''
		pass


