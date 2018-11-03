from django.shortcuts import render,reverse,redirect

from django.views.generic import View
from .forms import CheckLoginForm,CheckRegisterForm
from ..user.models import User
from hashlib import md5
from django.contrib.auth import login
# Create your views here.


class LoginView(View):
	'''
	用户登录在此处处理
	'''
	def __hashMD__(self,passWord):
		'''
		密码md5加密
		'''
		myhash = md5()
		myhash.update(bytes(str(passWord),encoding = 'utf-8'))
		return myhash.hexdigest()

	def get(self,request,*args,**kwargs):
		'''
		get请求
		'''

		return render(request,'login/login.html',{'user':CheckLoginForm()})

	def post(self,request,*args,**kwargs):
		'''
		post请求
		'''
		form = CheckLoginForm(request.POST)
		ok = form.is_valid()

		if ok:
			userID = form.cleaned_data['userID']
			password = self.__hashMD__(form.cleaned_data['password'])
			try:
				user = User.objects.get(userID = userID,password = password)
				login(request,user)
				if user and user.is_active:
					nextUrl = 'home:index'

					return redirect(reverse(nextUrl))
				else:
					return render(request,'login/login.html',{'user':CheckLoginForm(),'message':'请输入正确用户名和密码'})
			except:
				return render(request,'login/login.html',{'user':CheckLoginForm(),'message':'请输入正确用户名和密码'})

		return render(request,'login/login.html',{'user':CheckLoginForm(),'message':'请输入正确用户名和密码'})

class RegisterView(View):
	'''
	用户注册处理,包括发送邮件验证等
	'''
	def get(self,request):

		return render(request, "login/register.html",{'user':CheckRegisterForm()})

	def post(self,request):

		pass