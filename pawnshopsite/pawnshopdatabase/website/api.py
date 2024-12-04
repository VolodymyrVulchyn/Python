import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer, EmployeeSerializer, ItemSerializer, ItemCategorySerializer, PaymentSerializer, InventorySerializer, ItemPledgeSerializer, ReportSerializer, SoldItemSerializer, TransactionPaymentSerializer, RatedItemsSerializer, CreditSerializer
from rest_framework import viewsets
from .models import Customer, Employee, Item, ItemCategory, TransactionPayment, ItemPledge, SoldItem, RatedItem, Payment, Report, Inventory, Credit
from .repository import SoldItemRepository

class CustomerApi(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # http_method_names = ['get'] - якщо, хочемо використовувати один метод
    http_method_names = ['get', 'post', 'put', 'head', 'options', 'delete' ]

class EmployeeApi(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # http_method_names = ['get', 'post']
    http_method_names = ['get', 'post', 'put', 'head', 'options', 'delete']

class ItemApi(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCategoryApi(viewsets.ModelViewSet):
    queryset =  ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer

class PaymentApi(viewsets.ModelViewSet):
    queryset =  Payment.objects.all()
    serializer_class = PaymentSerializer

class InventoryApi(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class ItemPledgeApi(viewsets.ModelViewSet):
    queryset = ItemPledge.objects.all()
    serializer_class = ItemPledgeSerializer

class ReportApi(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class SoldItemApi(viewsets.ModelViewSet):
    queryset = SoldItem.objects.all()
    serializer_class = SoldItemSerializer

class TransactionPaymentApi(viewsets.ModelViewSet):
    queryset = TransactionPayment.objects.all()
    serializer_class = TransactionPaymentSerializer

class RatedItemsApi(viewsets.ModelViewSet):
    queryset = RatedItem.objects.all()
    serializer_class = RatedItemsSerializer

class CreditApi(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


# LAB4

class SoldItemReportApi(APIView):
    def get(self, request, *args, **kwargs):
        # Отримуємо агреговані дані по місяцях
        sales_data = SoldItemRepository.get_sales_per_month()


        df = pd.DataFrame(sales_data)


        return Response(df.to_json(orient="records"))

class SalesByEmployeeApi(APIView):
    def get(self, request, *args, **kwargs):

        sales_data = SoldItemRepository.get_sales_by_employee()


        df = pd.DataFrame(sales_data)


        return Response(df.to_json(orient="records"))

class SalesByCategoryApi(APIView):
    def get(self, request, *args, **kwargs):

        sales_data = SoldItemRepository.get_sales_by_category()


        df = pd.DataFrame(sales_data)


        return Response(df.to_json(orient="records"))

class AverageSalesByCustomerApi(APIView):
    def get(self, request, *args, **kwargs):

        sales_data = SoldItemRepository.get_average_sales_by_customer()


        df = pd.DataFrame(sales_data)


        return Response(df.to_json(orient="records"))

class SalesCountByItemApi(APIView):
    def get(self, request, *args, **kwargs):

        sales_data = SoldItemRepository.get_sales_count_by_item()


        df = pd.DataFrame(sales_data)


        return Response(df.to_json(orient="records"))

class MaxSalesByEmployeeApi(APIView):
    def get(self, request, *args, **kwargs):

        sales_data = SoldItemRepository.get_max_sale_by_employee()


        df = pd.DataFrame(sales_data)


        return Response(df.to_json(orient="records"))

from rest_framework.views import APIView

# class SoldItemReportApi(APIView):
#     def get(self, request):
#         data = {
#             'avg_sales_by_category': list(SoldItemRepository.get_sales_by_category()),
#             'sales_per_month': list(SoldItemRepository.get_sales_per_month()),
#             'sales_by_employee': list(SoldItemRepository.get_sales_by_employee()),
#             'average_sales_by_customer': list(SoldItemRepository.get_average_sales_by_customer()),
#             'sales_count_by_item': list(SoldItemRepository.get_sales_count_by_item()),
#             'max_sale_by_employee': list(SoldItemRepository.get_max_sale_by_employee()),
#             'avg_sales': SoldItemRepository.get_avg_sales(),
#             'min_sales': SoldItemRepository.get_min_sales(),
#             'max_sales': SoldItemRepository.get_max_sales()
#         }
#         return Response(data)




