from django.urls import path

#from .views import index, listar	
from . import views
urlpatterns = [
	path('verificarCodigoJson/<str:ean13>/', views.verificarCodigoJson, name='verificarCodigoJson'),
	path('listadoJson/', views.listadoJson, name='listadojson'),
	path('verificar/<str:ean13>/', views.verificarCodigo, name='verificarCodigo'),
	path('listar/', views.listar, name='listar'),
	path('', views.index, name='index'),
]