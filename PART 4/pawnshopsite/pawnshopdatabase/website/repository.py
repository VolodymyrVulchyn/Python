from django.db.models.functions import TruncMonth
from .models import Customer, Item, ItemCategory, Employee, Credit, SoldItem
from django.db.models import Count, Avg, Max, Min, Sum
class CustomerRepository:
    @staticmethod
    def get_all_customers():
        return Customer.objects.all()

    @staticmethod
    def get_customer_by_id(customer_id):
        return Customer.objects.get(id=customer_id)

    @staticmethod
    def add_customer(customer_data):
        customer = Customer(**customer_data)
        customer.save()
        return customer

class EmployeeRepository:
    @staticmethod
    def get_all_employees():
        return Employee.objects.all()

    @staticmethod
    def get_employee_by_id(employee_id):
        return Employee.objects.get(id=employee_id)

    @staticmethod
    def add_employee(employee_data):
        employee = Employee(**employee_data)
        employee.save()
        return employee

    @staticmethod
    def delete_employee(employee_id):
        employee = Employee.objects.get(id=employee_id)
        employee.delete()

class ItemRepository:
    @staticmethod
    def get_all_items():
        return Item.objects.all()

    @staticmethod
    def get_item_by_id(item_id):
        return Item.objects.get(item_id=item_id)

    @staticmethod
    def add_item(item_data):
        item = Item(**item_data)
        item.save()
        return item

    @staticmethod
    def delete_item(item_id):
        item = Item.objects.get(item_id=item_id)
        item.delete()

    @staticmethod
    def update_item(item_id, updated_data):
        item = Item.objects.get(item_id=item_id)
        for key, value in updated_data.items():
            setattr(item, key, value)
        item.save()
        return item

# --------------LAB-4--------------


# --------------LAB-4--------------

class ItemCategoryRepository:
    @staticmethod
    def get_all_categories():
        return ItemCategory.objects.all()

    @staticmethod
    def get_category_by_id(category_id):
        return ItemCategory.objects.get(id=category_id)

    @staticmethod
    def add_category(category_data):
        category = ItemCategory(**category_data)
        category.save()
        return category

    @staticmethod
    def delete_category(category_id):
        category = ItemCategory.objects.get(id=category_id)
        category.delete()

    @staticmethod
    def update_category(category_id, updated_data):
        category = ItemCategory.objects.get(id=category_id)
        for key, value in updated_data.items():
            setattr(category, key, value)
        category.save()
        return category

    # LAB4

from django.db.models import Avg, Min, Max, Count, Sum
from django.db.models.functions import TruncMonth
from .models import SoldItem

class SoldItemRepository:
    @staticmethod
    def get_sales_per_month():
        # Агрегуємо продажі по місяцях
        return SoldItem.objects.annotate(month=TruncMonth('date_sell')).values('month').annotate(
            total_sales=Sum('price_sell')).order_by('month')

    @staticmethod
    def get_sales_by_employee():
        # Агрегуємо продажі за кожним співробітником
        return SoldItem.objects.values('employee').annotate(total_sales=Sum('price_sell'),
                                                             count_sales=Count('sell_id')).order_by('-total_sales')

    @staticmethod
    def get_sales_by_category():
        # Агрегуємо продажі за категоріями товарів
        return SoldItem.objects.values('item_id').annotate(total_sales=Sum('price_sell')).order_by('-total_sales')

    @staticmethod
    def get_average_sales_by_customer():
        # Середня сума продажів по кожному клієнту
        return SoldItem.objects.values('user_pledge_id').annotate(average_sales=Avg('price_sell')).order_by('user_pledge_id')

    @staticmethod
    def get_sales_count_by_item():
        # Підраховуємо кількість продажів по кожному товару
        return SoldItem.objects.values('item').annotate(count_sales=Count('sell_id')).order_by('-count_sales')

    @staticmethod
    def get_max_sale_by_employee():
        # Максимальна сума продажу для кожного співробітника
        return SoldItem.objects.values('employee_id').annotate(max_sale=Max('price_sell')).order_by('-max_sale')

    @staticmethod
    def get_avg_sales():
        # Середнє значення продажів
        return SoldItem.objects.aggregate(average_sales=Avg('price_sell'))

    @staticmethod
    def get_min_sales():
        # Мінімальне значення продажів
        return SoldItem.objects.aggregate(min_sales=Min('price_sell'))

    @staticmethod
    def get_max_sales():
        # Максимальне значення продажів
        return SoldItem.objects.aggregate(max_sales=Max('price_sell'))