from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'inicio'

urlpatterns = [
    path('',login_required(views.index), name='index'),

    #/inicio/(nodo.id)/
    path('<int:nodo_id>/',login_required(views.nodo_detail) , name='nodo_detail'),
	#path('api/data/', views.get_data, name='get_data'), #pass data to view and then take those data

	#/inicio/(Nodo.id)/(Nodo.Variable)
	path('<int:nodo_id>/<str:nodo_var>/',login_required( views.nodo_variable), name='nodo_variable'),


]
