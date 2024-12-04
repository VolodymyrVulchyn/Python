from django.urls import path, include
from . import views
from rest_framework import routers
from .api import CustomerApi, EmployeeApi, ItemApi, ItemCategoryApi, RatedItemsApi, CreditApi, ReportApi, ItemPledgeApi, InventoryApi, PaymentApi, TransactionPaymentApi, SoldItemApi
from rest_framework_simplejwt.views import TokenRefreshView

#----LAB4----
from .api import (
    SoldItemReportApi,
    SalesByEmployeeApi,
    SalesByCategoryApi,
    AverageSalesByCustomerApi,
    SalesCountByItemApi,
    MaxSalesByEmployeeApi

)
#----LAB4----
from .views import LoginAPIView, SoldItemAllReportApi, dashboard_view

router = routers.DefaultRouter()
router.register(r'api/customer', CustomerApi)
router.register(r'api/employee', EmployeeApi)
router.register(r'api/item', ItemApi)
router.register(r'api/rated_item', ItemCategoryApi)
router.register(r'api/rated_item', RatedItemsApi)
router.register(r'api/credit', CreditApi)
router.register(r'api/report', ReportApi)
router.register(r'api/item_pledge', ItemPledgeApi)
router.register(r'api/inventory', InventoryApi)
router.register(r'api/payment', PaymentApi)
router.register(r'api/transaction_payment', TransactionPaymentApi)
router.register(r'api/sold_item', SoldItemApi)

# #----LAB4----
# router.register(r'api/sold_item/report/monthly', SoldItemReportApi, basename='sold_item_report_monthly')
# router.register(r'api/sold_item/report/employee', SalesByEmployeeApi, basename='sold_item_report_employee')
# router.register(r'api/sold_item/report/category', SalesByCategoryApi, basename='sold_item_report_category')
# router.register(r'api/sold_item/report/average_sales_customer', AverageSalesByCustomerApi, basename='sold_item_report_average_sales_customer')
# router.register(r'api/sold_item/report/count_sales_item', SalesCountByItemApi, basename='sold_item_report_count_sales_item')
# router.register(r'api/sold_item/report/max_sales_employee', MaxSalesByEmployeeApi, basename='sold_item_report_max_sales_employee')
# #----LAB4----


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

    path('login/', views.login_user, name='login'),

    # API urls

    path('', include(router.urls)),

    path('api/login/', LoginAPIView.as_view(), name='api-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/employee/', views.register_employee, name='register_employee'),
    path('api/register/customer/', views.register_customer, name='register_customer'),


# --------------LAB-4--------------
    path('api/sold_item/report/monthly/', SoldItemReportApi.as_view(), name='sold_item_report_monthly'),
    path('api/sold_item/report/employee/', SalesByEmployeeApi.as_view(), name='sold_item_report_employee'),
    path('api/sold_item/report/category/', SalesByCategoryApi.as_view(), name='sold_item_report_category'),
    path('api/sold_item/report/average_sales_customer/', AverageSalesByCustomerApi.as_view(), name='sold_item_report_average_sales_customer'),
    path('api/sold_item/report/count_sales_item/', SalesCountByItemApi.as_view(), name='sold_item_report_count_sales_item'),
    path('api/sold_item/report/max_sales_employee/', MaxSalesByEmployeeApi.as_view(), name='sold_item_report_max_sales_employee'),

# PART 2 LAB 4
    path('api/sold_item_all/report/', SoldItemAllReportApi.as_view(), name='sold_item_report'),

# PART 3 LAB 4
    path('dashboard/', dashboard_view, name='dashboard'),

]



