from django.shortcuts import render,reverse,redirect

from django.views.generic import View
from .forms import CheckLoginForm,CheckRegisterForm
from ..user.models import User
from hashlib import md5
from datetime import datetime
from django.contrib.auth import login
# Create your views here.

def __hashMD__(passWord):
	'''
	密码md5加密
	'''
	myhash = md5()
	myhash.update(bytes(str(passWord),encoding = 'utf-8'))
	return myhash.hexdigest()

class LoginView(View):
	'''
	用户登录在此处处理
	'''

	def get(self,request,*args,**kwargs):
		'''
		get请求
		'''

		return render(request,'login/login.html',{'user':CheckLoginForm()})

	def post(self,request):
		'''
		post请求
		'''
		form = CheckLoginForm(request.POST)
		ok = form.is_valid()
		print(form.cleaned_data)
		if ok:
			userID = form.cleaned_data['userID']
			password = __hashMD__(form.cleaned_data['password'])
			try:
				user = User.objects.get(userID = userID,password = password)

				if user and user.is_active:
					login(request,user)
					nextUrl = 'home:index'
					User.objects.update(last_login = datetime.now())
					response = redirect(reverse(nextUrl))
					response.delete_cookie('login')
					return response
				else:
					return render(request,'login/login.html',{'user':CheckLoginForm(),'message':'未激活'})
			except:
				
				return render(request,'login/login.html',{'user':CheckLoginForm(),'message':'请输入正确用户名和密码'})

		return render(request,'login/login.html',{'user':CheckLoginForm(),'message':'用户名和密码格式不正确'})

class RegisterView(View):
	'''
	用户注册处理,包括发送邮件验证等
	'''
	def get(self,request):

		return render(request, "login/register.html",{'user':CheckRegisterForm()})

	def post(self,request):
		'''
		未写邮件激活
		'''
		print(request.POST)
		form = CheckRegisterForm(request.POST)
		if not form.is_valid():
			
			return render(request, "login/register.html",{'user':CheckRegisterForm(),'message':'请输入正确的信息'})
		
		form.cleaned_data['password'] = __hashMD__(form.cleaned_data['password'])
		user = User(**form.cleaned_data)
		user.save()
		
		return render(request, "login/register.html",{'user':CheckRegisterForm(),'message':'注册成功,请返回登录'})
