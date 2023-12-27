from django.shortcuts import render
from django.views.generic import ListView, View
from catalog.models import Product, Category


class ProductListView(ListView):
    model = Product


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name is not None and email is not None:
            return render(request, 'catalog/contacts.html', context={'name': name, 'email': email})
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


class ProductView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'object_list': Product.objects.filter(id=pk),
        }
        return render(request, 'catalog/product.html', context)


class ProductCategoryListView(ListView):
    model = Product

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(product_category_id=category_pk)


class CategoryListView(ListView):
    model = Category
