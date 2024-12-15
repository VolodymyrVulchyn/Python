from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Customer, Employee, Item, ItemCategory, TransactionPayment, SoldItem, RatedItem, ItemPledge, Payment, Credit, Report, Inventory

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'


class TransactionPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionPayment
        fields = '__all__'

class SoldItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoldItem
        fields = '__all__'

class RatedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatedItem
        fields = '__all__'

class ItemPledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPledge
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email_or_username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)




