from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("Login.urls")),
    path("user/", include("Accounts.urls")),
    path('admin/', admin.site.urls),
]
