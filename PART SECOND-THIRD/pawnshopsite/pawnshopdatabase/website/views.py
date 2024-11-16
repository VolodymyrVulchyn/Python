from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token

from .models import Customer, Employee, Item, ItemCategory
from .forms import (
    CustomerRegistrationForm,
    EmployeeRegistrationForm,
    ItemForm,
    ItemCategoryForm,
    SearchForm,
    LoginUserForm,
)
from .repository import (
    CustomerRepository,
    EmployeeRepository,
    ItemRepository,
    ItemCategoryRepository,
)
from .serializers import LoginSerializer

# ---------------------------
# Утиліти
# ---------------------------

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {'refresh': str(refresh), 'access': str(refresh.access_token)}

# ---------------------------
# Функції для аутентифікації та авторизації
# ---------------------------

def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email_or_username = serializer.validated_data['email_or_username']
            password = serializer.validated_data['password']

            user = self._get_user(email_or_username, password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _get_user(self, email_or_username, password):
        if '@' in email_or_username:
            return self._get_user_by_email(email_or_username, password)
        return self._get_user_by_username(email_or_username, password)

    def _get_user_by_email(self, email, password):
        for model in [Customer, Employee]:
            try:
                user_obj = model.objects.get(email=email)
                if user_obj.check_password(password):
                    return user_obj.user if user_obj.user else self._create_user(user_obj)
            except model.DoesNotExist:
                continue
        return None

    def _get_user_by_username(self, username, password):
        for model in [Customer, Employee]:
            try:
                user_obj = model.objects.get(username=username)
                if user_obj.check_password(password):
                    return user_obj.user if user_obj.user else self._create_user(user_obj)
            except model.DoesNotExist:
                continue
        return None

    def _create_user(self, obj):
        user = get_user_model().objects.create_user(
            username=obj.username, email=obj.email, password=obj.password
        )
        obj.user = user
        obj.save()
        return user


@api_view(['POST'])
def login_user_api(request):
    email_or_username = request.data.get('email_or_username')
    password = request.data.get('password')

    user = get_user_model().objects.filter(
        email=email_or_username
    ).first() or get_user_model().objects.filter(username=email_or_username).first()

    if user and user.check_password(password):
        tokens = get_tokens_for_user(user)
        return Response({'message': 'Login successful', 'tokens': tokens}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid email/username or password'}, status=status.HTTP_400_BAD_REQUEST)

# ---------------------------
# Функції для роботи з клієнтами
# ---------------------------

def show_customers(request):
    customers = CustomerRepository().get_all_customers()
    return render(request, 'customers.html', {'customers': customers})


def add_customer(request):
    if request.method == 'POST':
        CustomerRepository.add_customer(request.POST.dict())
        return redirect('show_customers')
    return render(request, 'add_customer.html')


def delete_customer(request, customer_id):
    get_object_or_404(Customer, id=customer_id).delete()
    return redirect('customers_list')


def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register_customer.html', {'form': form})


# ---------------------------
# Функції для роботи з працівниками
# ---------------------------

def show_employees(request):
    employees = EmployeeRepository().get_all_employees()
    return render(request, 'employees.html', {'employees': employees})


def delete_employee(request, employee_id):
    get_object_or_404(Employee, id=employee_id).delete()
    return redirect('employee_list')


def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'register_employee.html', {'form': form})


# ---------------------------
# Функції для роботи з предметами
# ---------------------------

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


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})


def delete_item(request, item_id):
    ItemRepository.delete_item(item_id)
    return redirect('items_list')


# ---------------------------
# Функції для роботи з категоріями
# ---------------------------

def show_categories(request):
    categories = ItemCategory.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def add_category(request):
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = ItemCategoryForm()
    return render(request, 'add_category.html', {'form': form})


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


def delete_category(request, category_id):
    ItemCategoryRepository.delete_category(category_id)
    return redirect('categories_list')


# ---------------------------
# Пошук
# ---------------------------

def search_view(request):
    form = SearchForm()
    result = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            model_choice = form.cleaned_data['model']
            object_id = form.cleaned_data['id']

            repo_map = {
                'customer': CustomerRepository.get_customer_by_id,
                'employee': EmployeeRepository.get_employee_by_id,
                'item': ItemRepository.get_item_by_id,
                'category': ItemCategoryRepository.get_category_by_id,
            }
            try:
                result = repo_map[model_choice](object_id)
            except KeyError:
                result = f'{model_choice.capitalize()} not found'

    return render(request, 'search.html', {'form': form, 'result': result})


# ---------------------------
# Головна сторінка
# ---------------------------

def home(request):
    return render(request, 'home.html', {})