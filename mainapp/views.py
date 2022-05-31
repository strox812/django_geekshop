from django.shortcuts import render
from django.shortcuts import get_object_or_404


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

#  урок 5
def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content)


    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products
    }

    return render(request, 'mainapp/products.html', content)

