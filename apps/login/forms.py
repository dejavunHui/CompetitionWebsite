from django.forms import ModelForm,PasswordInput
from ..user.models import User

class CheckLoginForm(ModelForm):
	'''
	检查用户登录表单是否正确
	'''

	class Meta:
		model = User
		fields = ['userID','password']
		widgets = {
			'passWord':PasswordInput(attrs={'cols':20,'rows':10})
		}


class CheckRegisterForm(ModelForm):
	'''
	检查用户注册信息
	'''
	class Meta:

		model = User
		fields = ['userID','userName','password','userEmail','userPhone',
					'userSex','userNo','userSchool']
		widgets = {
			'passWord':PasswordInput(attrs={'cols':20,'rows':10}),
		}