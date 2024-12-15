from .models import Customer, Item, ItemCategory, Employee

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