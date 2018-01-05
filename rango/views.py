from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'rango/index.html')

def about(request):
	return render(request, 'rango/about.html')