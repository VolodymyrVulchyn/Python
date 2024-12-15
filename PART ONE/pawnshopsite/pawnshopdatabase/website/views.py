
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Employee
from .forms import CustomerRegistrationForm, EmployeeRegistrationForm, ItemForm, ItemCategoryForm, ItemCategory, Item, SearchForm
from .repository import CustomerRepository, EmployeeRepository, ItemRepository, ItemCategoryRepository



def home(request):
    return render(request, 'home.html', {})

def show_customers(request):
    customer_repo = CustomerRepository()
    customers = customer_repo.get_all_customers()
    return render(request, 'customers.html', {'customers': customers})

def add_customer(request):
    if request.method == 'POST':
        customer_data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'phone_number': request.POST.get('phone_number'),
            'city': request.POST.get('city'),
            'address': request.POST.get('address'),
            'email': request.POST.get('email'),
            'number_document': request.POST.get('number_document'),
            'date_birthday': request.POST.get('date_birthday'),
            'gender': request.POST.get('gender'),
        }
        CustomerRepository.add_customer(customer_data)
        return redirect('show_customers')
    return render(request, 'add_customer.html')



def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('customers_list')

def show_employees(request):
    employee_repo = EmployeeRepository()
    employees = employee_repo.get_all_employees()
    return render(request, 'employees.html', {'employees': employees})


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # зберігає нового користувача в базі даних
            return redirect('customers_list')  # перенаправляє на сторінку входу або іншу сторінку
    else:
        form = CustomerRegistrationForm()

    return render(request, 'register_customer.html', {'form': form})


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # зберігає нового працівника в базі даних
            return redirect('employee_list')  # перенаправляє на сторінку входу або іншу сторінку
    else:
        form = EmployeeRegistrationForm()

    return render(request, 'register_employee.html', {'form': form})

def show_items(request):
    items = ItemRepository.get_all_items()
    return render(request, 'items.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            ItemRepository.add_item(form.cleaned_data)
            return redirect('items_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def delete_item(request, item_id):
    ItemRepository.delete_item(item_id)
    return redirect('items_list')

def show_categories(request):
    categories = ItemCategoryRepository.get_all_categories()
    return render(request, 'categories.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST)
        if form.is_valid():
            ItemCategoryRepository.add_category(form.cleaned_data)
            return redirect('categories_list')
    else:
        form = ItemCategoryForm()
    return render(request, 'add_category.html', {'form': form})

def delete_category(request, category_id):
    ItemCategoryRepository.delete_category(category_id)
    return redirect('categories_list')

def add_category(request):
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST)
        if form.is_valid():
            form.save()  # зберігає нову категорію в базі даних
            return redirect('categories_list')  # перенаправляє на сторінку з усіма категоріями
    else:
        form = ItemCategoryForm()

    return render(request, 'add_category.html', {'form': form})

def show_categories(request):
    categories = ItemCategory.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def edit_item(request, item_id):
    item = get_object_or_404(Item, item_id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})

def edit_category(request, category_id):
    category = get_object_or_404(ItemCategory, id=category_id)
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = ItemCategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form, 'category': category})

def search_view(request):
    result = None
    form = SearchForm()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            model_choice = form.cleaned_data['model']
            object_id = form.cleaned_data['id']

            # Based on model selection, get the corresponding object
            if model_choice == 'customer':
                try:
                    result = CustomerRepository.get_customer_by_id(object_id)
                except Customer.DoesNotExist:
                    result = 'Customer not found'
            elif model_choice == 'employee':
                try:
                    result = EmployeeRepository.get_employee_by_id(object_id)
                except Employee.DoesNotExist:
                    result = 'Employee not found'
            elif model_choice == 'item':
                try:
                    result = ItemRepository.get_item_by_id(object_id)
                except Item.DoesNotExist:
                    result = 'Item not found'
            elif model_choice == 'category':
                try:
                    result = ItemCategoryRepository.get_category_by_id(object_id)
                except ItemCategory.DoesNotExist:
                    result = 'Category not found'

    return render(request, 'search.html', {'form': form, 'result': result})




