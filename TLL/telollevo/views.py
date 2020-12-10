from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from telollevo.models import Envios
from django.http import HttpResponse
from .forms import EnviosForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def error_facebook(request):
	return render(request, 'registration/error_facebook.html')

def home(request):
	return render(request, 'telollevo/home.html')

def faqs(request):
	return render(request, 'telollevo/faqs.html')

def galeria(request):
	return render(request, 'telollevo/galeria.html')

def mensaje(request):
	return render(request, 'telollevo/mensaje.html')

def siguetuenvio(request):
	return render(request, 'telollevo/siguetuenvio.html')

def buscar(request):
	if request.GET["idenv"]:
		envio = request.GET["idenv"]

		info = Envios.objects.filter(id__icontains=envio)

		return render(request, "telollevo/siguetuenvio_details.html", {"info":info, "query":envio})

def agregarEnvio(request):
	data = {
		'form': EnviosForm()
	}

	if request.method == 'POST':
		formulario = EnviosForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()

			asunto = "Tu ID de Envio - Te Lo Llevo"
			mensaje  = "Hola " + request.POST["nombreDestino"] + "\n\nSe generado una orden de envio a tu nombre, tu ID de envio es:\n\n" + request.POST["id"] + "\n\nCon este codigo puedes consultar el estado e informacion de tu envio desde nuestra pagina"
			desde = settings.EMAIL_HOST_USER
			hacia = [request.POST["correoDestino"]]

			send_mail(asunto, mensaje, desde, hacia, fail_silently=False)

			
			data["mensaje"] = "\n\nGuardado Correctamente\n\n"

			data["form"] = formulario

	return render(request, "telollevo/agregarEnvio.html", data)

def listarEnvio(request):
	envios = Envios.objects.all()
	data = {
		'envios': envios
	}
	return render(request, "telollevo/listarEnvio.html", data)

def modificarEnvio(request, id):
	envio = get_object_or_404(Envios, id=id)

	data = {
		'form': EnviosForm(instance=envio)
	}

	if request.method == "POST":
		formulario = EnviosForm(data=request.POST, instance=envio)
		if formulario.is_valid():
			formulario.save()
			return redirect(to="listarEnvio")
		data["form"] = formulario

	return render(request, "telollevo/modificarEnvio.html", data)

def eliminarEnvio(request, id):
	envio = get_object_or_404(Envios, id = id)
	envio.delete()
	return redirect(to="listarEnvio")