from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from adminapp.forms import UserAdminEditForm, ProductEditForm
from authapp.models import ShopUser
from mainapp.models import Category, Product
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin


class AccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    return None

# @user_passes_test(lambda u: u.is_superuser)
# def user_read(request):
#     context = {
#         'objects': ShopUser.objects.all().order_by('is_active', 'is_superuser')
#     }
#     return render(request, 'adminapp/user_list.html', context)


class UserListView(AccessMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/user_list.html'
    paginate_by = 2

    extra_context = {
        'title': 'Список пользователей'
    }



# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     user_item = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = UserAdminEditForm(request.POST, request.FILES, instance=user_item)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('adminapp:user_update', args=[pk]))
#     else:
#         edit_form = UserAdminEditForm(instance=user_item)
#
#     context = {
#         'form': edit_form
#     }
#     return render(request, 'adminapp/user_form.html', context)

class UserUpdateView(AccessMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = UserAdminEditForm

    def get_success_url(self):
        return reverse('adminapp:user_update', args=[self.kwargs.get('pk')])


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user_item = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_item.is_active = False
        user_item.save()
        return HttpResponseRedirect(reverse('adminapp:user_read'))


    context = {
        'object': user_item
    }
    return render(request, 'adminapp/user_delete_confirm.html', context)

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    return None

@user_passes_test(lambda u: u.is_superuser)
def category_read(request):
    context = {
        'objects_list': Category.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/category_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    return None

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    return None

@user_passes_test(lambda u: u.is_superuser)
def products_read(request, pk):
    category_item = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category_id=pk)
    context = {
        'objects_list': products_list,
        'category': category_item
    }
    return render(request, 'adminapp/products_list.html', context)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    category_item = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_item = product_form.save()
            return HttpResponseRedirect(reverse('adminapp:products_read', args=[product_item.category.pk]))
    else:
        product_form = ProductEditForm()
    context = {
        'form': product_form
    }
    return render(request, 'adminapp/product_form.html', context)

@user_passes_test(lambda u: u.is_superuser)
def product_update(request):
    return None

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request):
    return None

@user_passes_test(lambda u: u.is_superuser)
def product_detail(request):
    return None
