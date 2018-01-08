from django.shortcuts import render
from .models import Category

# Create your views here.

def index(request):
	categories = Category.objects.order_by('name')
	context = { 'italicmessage': 'I am italic!',
				'categories': categories }
	return render(request, 'rango/index.html', context)

def about(request):
	context = { 'boldmessage': 'I am bold text!' }
	return render(request, 'rango/about.html', context)