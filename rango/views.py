from django.shortcuts import render, get_object_or_404
from .models import Category, Page

# Create your views here.

def index(request):
	categories = Category.objects.order_by('name')
	pages = Page.objects.order_by('-views')
	context = { 'italicmessage': 'I am italic!',
				'categories': categories,
			    'pages': pages }
	return render(request, 'rango/index.html', context)

def about(request):
	context = { 'boldmessage': 'I am bold text!' }
	return render(request, 'rango/about.html', context)

def category(request, category_name_slug):
	category = get_object_or_404(Category, slug = category_name_slug)
	pages = Page.objects.filter(category = category)
	context = { 'category': category, 'pages': pages }
	return render(request, 'rango/category.html', context)