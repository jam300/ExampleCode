from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import  login,logout_then_login


urlpatterns = [

    path('admin/', admin.site.urls),
    path('inicio/', include('inicio.urls')),
    path('accounts/login/', login,{'template_name':'login.html'}, name='login'),
    path('', logout_then_login, name='logout'),

]
