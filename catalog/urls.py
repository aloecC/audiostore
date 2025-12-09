from django.urls import path
from . import views
from .views import ContactsTemplateView, ProductDetailView, ProductListView, CategoryListView, CategoryDetailView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView

#Пространство имен(помогает избежать ошибки при одинаковых именах маршрута)
app_name = 'catalog'

#В urlpatterns создаются и регестрируются маршруты
#Path это специальная функция которая позволяет регестрировать наш маршрут
urlpatterns = [
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('home/', ProductListView.as_view(), name='product_list'),
    path('product/new/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('catalogs/', CategoryListView.as_view(), name='category_list'),
    path('category_detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    ]