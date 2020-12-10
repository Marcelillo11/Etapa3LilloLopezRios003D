from django.urls import path
from .views import home, faqs, galeria, mensaje, siguetuenvio, buscar, agregarEnvio, listarEnvio, modificarEnvio, eliminarEnvio, error_facebook
from telollevo import views

urlpatterns=[
	path('', home, name="home"),
	path('faqs/', faqs, name="faqs"),
	path('galeria/', galeria, name="galeria"),
	path('mensaje/', mensaje, name="mensaje"),
	path('siguetuenvio/', siguetuenvio, name="siguetuenvio"),
	path('buscar/', buscar, name="buscar"),
	path('agregarEnvio/', agregarEnvio, name="agregarEnvio"),
	path('listarEnvio/', listarEnvio, name="listarEnvio"),
	path('modificarEnvio/<id>', modificarEnvio, name="modificarEnvio"),
	path('eliminarEnvio/<id>', eliminarEnvio, name="eliminarEnvio"),
	path('error-facebook/', error_facebook, name="error_facebook"),
]