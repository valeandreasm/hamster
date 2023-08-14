from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Usuario
from .forms import FormUsuario
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def sobre_mi(request):
    return render(request, 'sobre_mi.html')

def form(request):
	if request.method == 'POST':
		form = FormUsuario(request.POST)
		if form.is_valid():
			usuario = Usuario.objects.create(**form.cleaned_data)
		return HttpResponseRedirect('/')
	else:
		form = FormUsuario()
	return render(request, 'form.html', {'form':form})