from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, View, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Category, Version
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from catalog.services import get_categories_cache


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_active=True)
        context['active_versions'] = active_versions

        return context


class ContactView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')


@login_required
def home(request):
    return render(request, 'catalog/home.html')


class ProductView(LoginRequiredMixin, View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'object_list': Product.objects.filter(id=pk),
        }
        return render(request, 'catalog/product.html', context)


class ProductCategoryListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return Product.objects.filter(product_category_id=category_pk)


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = get_categories_cache()
        return context_data


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        return self.request.user.is_superuser
