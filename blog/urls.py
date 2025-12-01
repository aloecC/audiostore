from django.urls import path
from . import views
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

#Пространство имен(помогает избежать ошибки при одинаковых именах маршрута)
app_name = 'blog'

#В urlpatterns создаются и регестрируются маршруты
#Path это специальная функция которая позволяет регестрировать наш маршрут
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
