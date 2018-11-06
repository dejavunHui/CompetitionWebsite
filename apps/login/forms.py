from django.forms import ModelForm,PasswordInput,Form
from django import forms

from ..user.models import User

class CheckLoginForm(Form):
	'''
	检查用户登录表单是否正确
	'''
	userID = forms.CharField(max_length=120)
	password = forms.CharField(max_length=120,widget = PasswordInput(attrs={'cols':20,'rows':10}))

	def clean(self):
		cleaned_data = super(CheckLoginForm,self).clean()

		return cleaned_data

class CheckRegisterForm(ModelForm):
	'''
	检查用户注册信息
	'''
	class Meta:

		model = User
		fields = ['userID','userName','password','userEmail','userPhone',
					'userSex','userNo','userSchool']
		widgets = {
			'password':PasswordInput(attrs={'cols':20,'rows':10}),
		}