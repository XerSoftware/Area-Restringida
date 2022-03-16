import json
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
# Create your views here.
from .models import CodigoAcceso
8
app_name = 'accesoRestringido'
def index(request):
	return HttpResponse("Xerver Inicializado")

def listar(request):
	listado_completo = CodigoAcceso.objects.all()
	#return HttpResponse(listado_completo)
	return render(
        request,
        'listar.html',
        context={'ean13':listado_completo},
        )

def verificarCodigo(request, ean13):
	try:
		result = CodigoAcceso.objects.get(ean13=ean13)
	except CodigoAcceso.DoesNotExist:
		#raise Http404("Acceso Denegado")
		return HttpResponse("Acceso Denegado")
	return HttpResponse("Acceso Permitido")

def listadoJson(request):
	responseData = []
	for x in CodigoAcceso.objects.all():
		data = {
			'ean13': str(x),
		}
		responseData.append(data)
	return HttpResponse(json.dumps(responseData), content_type="application/json")

def verificarCodigoJson(request,ean13):
	try:
		result = CodigoAcceso.objects.get(ean13=ean13)
	except CodigoAcceso.DoesNotExist:
		data = {'permiso' : 0}
		return HttpResponse(json.dumps(data), content_type="application/json")
	data = {'permiso' : 1}
	return HttpResponse(json.dumps(data), content_type="application/json")