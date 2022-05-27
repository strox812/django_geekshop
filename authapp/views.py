from django.shortcuts import render


def login(request):

    return render(request, 'authapp/login.html')


def logout(request):
    pass


def register(request):

    return render(request, 'authapp/register.html')


def edit(request):

    return render(request, 'authapp/edit.html')
