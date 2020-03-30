from django.shortcuts import render
from django.views import View
# Create your views here.

class UserView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Accounts/profile.html', locals())
