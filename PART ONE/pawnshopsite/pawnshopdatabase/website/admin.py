from django.contrib import admin
from .models import Customer, Employee, TransactionPayment, Item, Payment, SoldItem, RatedItem, ItemPledge, ItemCategory, Credit, Report, Inventory

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(TransactionPayment)
admin.site.register(Item)
admin.site.register(Payment)
admin.site.register(SoldItem)
admin.site.register(RatedItem)
admin.site.register(ItemPledge)
admin.site.register(ItemCategory)
admin.site.register(Credit)
admin.site.register(Report)
admin.site.register(Inventory)
