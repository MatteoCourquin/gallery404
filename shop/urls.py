from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_view, name='create'),
    path('<id>/', views.detail_view, name='product'),
    path('<id>/update/', views.update_view, name='update'),
    path('<id>/delete/', views.delete_view, name='delete'),
]
