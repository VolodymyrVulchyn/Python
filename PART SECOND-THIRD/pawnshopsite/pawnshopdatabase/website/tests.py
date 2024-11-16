# # from django.test import TestCase
# # from .repository import CustomerRepository
# # from .models import Customer
# #
# #
# # class CustomerRepositoryTest(TestCase):
# #
# #     def test_add_customer(self):
# #         # Дані для створення користувача
# #         customer_data = {
# #             'first_name': 'Andrii',
# #             'last_name': 'Shelep',
# #             'phone_number': '0976550102',
# #             'city': 'Sheptisctiky',
# #             'address': 'Graboskogo 15',
# #             'email': 'andrii.shelep.shi.2023@lpnu.ua',
# #             'number_document': 'AB1234567',
# #             'date_birthday': '2024-07-21',
# #             'gender': 'None'
# #         }
# #
# #         # Створюємо репозиторій
# #         customer_repo = CustomerRepository()
# #
# #         # Додаємо користувача через репозиторій
# #         customer = customer_repo.add_customer(customer_data)
# #
# #         # Перевіряємо, чи дані збереглись коректно
# #         self.assertEqual(customer.first_name, 'Andrii')
# #         self.assertEqual(customer.last_name, 'Shelep')
# #         self.assertEqual(customer.phone_number, '0976550102')
# #         self.assertEqual(customer.city, 'Sheptisctiky')
# #         self.assertEqual(customer.address, 'Graboskogo 15')
# #         self.assertEqual(customer.email, 'andrii.shelep.shi.2023@lpnu.ua')
# #         self.assertEqual(customer.number_document, 'AB1234567')
# #         self.assertEqual(str(customer.date_birthday), '2024-07-21')  # Перевірка формату дати
# #         self.assertEqual(customer.gender, 'None')
# #
# #         # Перевіряємо, чи користувач збережений у базі даних
# #         customer_from_db = Customer.objects.get(id=customer.id)
# #
# #         # Перевірка того, що отриманий з бази користувач має правильні дані
# #         self.assertEqual(customer_from_db.first_name, 'Andrii')
# #         self.assertEqual(customer_from_db.last_name, 'Shelep')
# #         self.assertEqual(customer_from_db.phone_number, '0976550102')
# #         self.assertEqual(customer_from_db.city, 'Sheptisctiky')
# #         self.assertEqual(customer_from_db.address, 'Graboskogo 15')
# #         self.assertEqual(customer_from_db.email, 'andrii.shelep.shi.2023@lpnu.ua')
# #         self.assertEqual(customer_from_db.number_document, 'AB1234567')
# #         self.assertEqual(str(customer_from_db.date_birthday), '2024-07-21')
# #         self.assertEqual(customer_from_db.gender, 'None')
#
#
# from django.test import TestCase
# from .repository import CustomerRepository, EmployeeRepository
# from .models import Customer, Employee, Item
#
# class RepositoryTests(TestCase):
#
#     def test_add_customer(self):
#         customer_data = {
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'phone_number': '123-456-789',
#             'city': 'New York',
#             'address': '123 Main St',
#             'email': 'john.doe@example.com',
#             'number_document': 'A123456789',
#             'date_birthday': '1980-01-01',
#             'gender': 'Male',
#         }
#         customer = CustomerRepository.add_customer(customer_data)
#         self.assertEqual(customer.first_name, 'John')
#         self.assertEqual(customer.last_name, 'Doe')
#
#     def test_get_all_customers(self):
#         customers = CustomerRepository.get_all_customers()
#         self.assertGreater(customers.count(), 0)
#
#     def test_add_employee(self):
#         employee_data = {
#             'first_name': 'Jane',
#             'last_name': 'Smith',
#             'phone_number': '987-654-321',
#             'city': 'Los Angeles',
#             'address': '456 Elm St',
#             'email': 'jane.smith@example.com',
#             'appointment': 'Manager',
#             'hire_date': '2020-05-15',
#             'salary': 50000.00,
#         }
#         employee = EmployeeRepository.add_employee(employee_data)
#         self.assertEqual(employee.first_name, 'Jane')
#         self.assertEqual(employee.last_name, 'Smith')
#
#     # def test_add_product(self):
#     #     category = ItemCategory.objects.create(type_item='Electronics', info_item='Devices')
#     #     product_data = {
#     #         'name_product': 'Laptop',
#     #         'info_product': 'A high-performance laptop.',
#     #         'category': category,
#     #         'appraised_value': 1000.00,
#     #         'serial_number': 'SN123456789',
#     #         'production_date': '2022-01-01',
#     #         'brand': 'BrandX',
#     #         'model': 'ModelY',
#     #         'photo_link': 'https://example.com/photo.jpg',
#     #     }
#     #     product = ProductRepository.add_product(product_data)
#     #     self.assertEqual(product.name_product, 'Laptop')
#     #     self.assertEqual(product.brand, 'BrandX')
