from django.shortcuts import render
from .models import Nodo,Variable
from django.db.models import Sum

#from django.http import JsonResponse
#import json

# def get_data(request, *args, **kwargs):
# 	El_Nodo = Nodo.objects.get(pk=1)
# 	elemento = El_Nodo.variable_set.order_by('pk').all()
# 	chartData = [{"date": str(t.Data_time.year) + "-" + str(t.Data_time.month) + "-" + str(t.Data_time.day) + " " + str(
# 		t.Data_time.hour) + ":" + str(t.Data_time.minute) + ":" + str(t.Data_time.second), "value": str(t.Watts),
# 	              "volume": str(t.Watts)} for t in elemento]
#
# 	data = {'chartData': chartData}
# 	return  JsonResponse (chartData)

def get_data(nodo_pk,magnitud):
	all_nodos = Nodo.objects.order_by('pk').all()  #get all nodos
	if nodo_pk ==1:
		El_Nodo = all_nodos.first()  #get Nodo.Nombre for current nodo view
	else:
		El_Nodo = all_nodos.get(pk=nodo_pk1)
	elemento = El_Nodo.variable_set.order_by('Data_time').all() # get all data from current nodo

	var = Variable()
	list_atributo = dir(var)   # get a lis of attribute for Variable model

	if magnitud =="Voltaje" or magnitud =="Corriente" or magnitud =="FP":
		Gauge_Variable = getattr(elemento.latest('Data_time'), magnitud)
	elif magnitud == "Watts" or magnitud == "VA" or magnitud =="VAR":
		val=elemento.aggregate(dt=Sum(magnitud))
		Gauge_Variable = val['dt']

	chartData = [{"date": str(t.Data_time.year) + "-" + str(t.Data_time.month) + "-" + str(t.Data_time.day) + " " + str(
		t.Data_time.hour) + ":" + str(t.Data_time.minute) + ":" + str(t.Data_time.second), "value": str(getattr(t,magnitud)),
	              "volume": str(getattr(t,magnitud))} for t in elemento]  # make JSON for amChart

	context = {'all_nodos': all_nodos,
	           'El_Nodo':El_Nodo,
	           'magnitud':magnitud,
	           'list_atributo':list_atributo,
	           'Gauge_Variable':Gauge_Variable,
	           'chartData': chartData }
	return  context

def index(request):
	return render(request,'inicio/index.html', get_data(1, "Watts"))

def nodo_detail(request,nodo_id):
	return render (request, 'inicio/detail.html', context=get_data(nodo_id,"Watts"))

def nodo_variable (request,nodo_id,nodo_var):
	return render(request, 'inicio/variable.html', get_data(nodo_id, nodo_var))