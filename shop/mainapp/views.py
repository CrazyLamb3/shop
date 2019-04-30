from django.shortcuts import render
from .models import Product, ProductCategory

def main(request):
    context = {'copyrigth': {'rigth': 'all rigth reserved'}}
    return render(request, 'mainapp/index.html', context)

def products(request,pk = None):
    # Product.objects.filter(category=pk)
    context = {'products': Product.objects.all(), 'categories': ProductCategory.objects.all()}
    return render(request, 'mainapp/catalog.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def registration(request):
    return render(request, 'mainapp/registration.html')

