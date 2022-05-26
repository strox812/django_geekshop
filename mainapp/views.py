from django.shortcuts import render
def index(request):
    context = {
        'products': Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)


def products(request):

    context = {
        'links_menu': Category.objects.all()
    }

    return render(request, 'mainapp/products.html', context)


def products_list(request, pk):
    context = {
        'links_menu': Category.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    return render(request, 'mainapp/contact.html')

from .models import Category, Product

def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)