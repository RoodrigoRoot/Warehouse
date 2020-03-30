from django.shortcuts import render
from django.views import View
from .forms import LoginUser
# Create your views here.

    
class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginUser()
        return render(request, 'login/login.html', locals())