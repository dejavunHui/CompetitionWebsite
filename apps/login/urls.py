from django.urls import path
from .views import LoginView,RegisterView

app_name = 'login'

urlpatterns = [
	path('login/',LoginView.as_view(),name = 'index'),
	path('register/',RegisterView.as_view(),name = 'register')
]