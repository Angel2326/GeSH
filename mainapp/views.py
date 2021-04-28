from django.shortcuts import render
from mainapp.models import Product, ProductCategory

# Create your views here.
# def index(request):
#     return render(request, 'mainapp/index.html')


def index(request):
    index_context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', index_context)


# def products(request):
#     return render(request, 'mainapp/products.html')


def products(request):
    products_context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', products_context)
