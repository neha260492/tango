from django.shortcuts import render

# Create your views here.

def index(request):
	context = { 'italicmessage': 'I am italic!' }
	return render(request, 'rango/index.html', context)

def about(request):
	context = { 'boldmessage': 'I am bold text!' }
	return render(request, 'rango/about.html', context)