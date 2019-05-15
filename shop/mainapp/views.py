from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket

def main(request):
    context = {'copyrigth': {'rigth': 'all rigth reserved'}}
    return render(request, 'mainapp/index.html', context)

def products(request,pk = None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        get_object_or_404(ProductCategory, pk=pk)
        product_objects = Product.objects.filter(category=pk)
    else:
        product_objects = Product.objects.all()
    context = {
        'categories': ProductCategory.objects.all(),
        'products': product_objects,
        'basket': basket
    }
    return render(request, 'mainapp/catalog.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')
#
# def registration(request):
#     return render(request, 'mainapp/registration.html')

