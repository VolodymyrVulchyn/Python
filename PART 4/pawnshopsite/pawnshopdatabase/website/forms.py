from django import forms
from .models import Customer, Employee, Item, ItemCategory, Credit

# Форма для реєстрації користувача як Customer
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name", "last_name", "phone_number", "city", "address", "email", "number_document", "date_birthday", "gender", "password"
                  ]

# Форма для реєстрації користувача як Employee
class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "first_name", "last_name", "phone_number", "city", "address", "email", "appointment", "hire_date", "salary", "password"
                  ]
# Форма для Items
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name_product", "info_product", "category", "appraised_value",
            "serial_number", "production_date", "brand", "model", "photo_link"
        ]

# Форма для ItemCategory
class ItemCategoryForm(forms.ModelForm):
    class Meta:
        model = ItemCategory
        fields = [
            "type_item", "info_item"
        ]

# Форма для Credit
class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = [
            "credit_id", "item_id", "client", "sum_loan", "percent_rate", "start_date", "end_date", "loan_status"
        ]


# Форма для Search
class SearchForm(forms.Form):
    model_choices = [
        ('customer', 'Customer'),
        ('employee', 'Employee'),
        ('item', 'Item'),
        ('category', 'Item Category'),
        ('credit', 'Credit')
    ]
    model = forms.ChoiceField(choices=model_choices, label="Select Model")
    id = forms.IntegerField(label="Enter ID", widget=forms.NumberInput(attrs={'placeholder': 'ID'}))

    def clean_id(self):
        id = self.cleaned_data.get('id')
        if id <= 0:
            raise forms.ValidationError("ID must be a positive integer.")
        return id

# Форма для LoginUser
class LoginUserForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
