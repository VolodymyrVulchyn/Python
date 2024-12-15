from .serializers import CustomerSerializer, EmployeeSerializer, ItemSerializer, ItemCategorySerializer, PaymentSerializer, InventorySerializer, ItemPledgeSerializer, ReportSerializer, SoldItemSerializer, TransactionPaymentSerializer, RatedItemsSerializer, CreditSerializer
from rest_framework import viewsets
from .models import Customer, Employee, Item, ItemCategory, TransactionPayment, ItemPledge, SoldItem, RatedItem, Payment, Report, Inventory, Credit

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