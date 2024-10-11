from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name='list_view'),
    path('list/<int:list_id>/', views.list_detail, name='list_detail'),
    path('list/<int:list_id>/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('list/<int:list_id>/delete/<int:item_id>/', views.delete_item, name='delete_item'),
]