from django.urls import path
from catalog.views import contact, home, ProductListView, ProductView, ProductCategoryListView, CategoryListView


urlpatterns = [
    path('product_list/', ProductListView.as_view()),
    path('contacts/', contact),
    path('', home),
    path('product/<int:pk>/', ProductView.as_view(), name='product'),
    path('product_list/<int:pk>/', ProductCategoryListView.as_view(), name='product_list'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
]