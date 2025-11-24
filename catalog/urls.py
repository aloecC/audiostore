from django.urls import path
from . import views

#Пространство имен(помогает избежать ошибки при одинаковых именах маршрута)
app_name = 'catalog'

#В urlpatterns создаются и регестрируются маршруты
#Path это специальная функция которая позволяет регестрировать наш маршрут
urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalogs/', views.catalogs, name='catalog'),
    path('product_detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('home/', views.product_list, name='product_list'),
    path('catalogs/', views.category_list, name='category_list')
    ]