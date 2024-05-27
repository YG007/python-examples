from django.urls import path
from books import views

urlpatterns = [
    path('knock-knock/', views.knock_knock, name='knock_knock'),
    path('books/', views.book_create_list, name='book_create_list'),
    path('books/<int:pk>/', views.book_detail_update_delete, name='book_detail_update_delete'),
    path('books/<int:pk>/stock', views.book_adjust_stock, name="book_adjust_stock")
]
