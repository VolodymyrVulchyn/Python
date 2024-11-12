from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),

    # Шляхи для клієнтів
    path('customers/', views.show_customers, name='customers_list'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),

    # Шляхи для співробітників
    path('employees/', views.show_employees, name='employee_list'),
    path('employees/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/employee/', views.register_employee, name='register_employee'),

    # Item URLs
    path('items/', views.show_items, name='items_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),

    # ItemCategory URLs
    path('categories/', views.show_categories, name='categories_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),

    path('categories/add/', views.add_category, name='add_category'),  # URL для додавання категорії
    path('categories/', views.show_categories, name='categories_list'),  # URL для перегляду категорій

    # Item edit URL
    path('items/edit/<int:item_id>/', views.edit_item, name='edit_item'),

    # Category edit URL
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),

    # Search by id
    path('search/', views.search_view, name='search'),


]
