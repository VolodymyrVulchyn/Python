from faker import Faker
import random
from website.models import Employee, Customer, Credit, Item, ItemCategory, Inventory, ItemPledge, Payment, RatedItem, Report, SoldItem, TransactionPayment

fake = Faker()

# Функція для перевірки довжини значень
def check_length(value, max_length):
    """Функція для перевірки довжини значення"""
    return value[:max_length] if len(value) > max_length else value

# Список категорій товарів для ломбарду
item_categories = ['Jewelry', 'Electronics', 'Musical Instruments', 'Tools', 'Watches', 'Collectibles', 'Vehicles', 'Furniture', 'Luxury Goods']

# Створення об'єктів
for _ in range(100):  # Створити 100 записів для кожної таблиці

    # Для Customer
    first_name_value = fake.first_name()
    last_name_value = fake.last_name()
    phone_number_value = fake.phone_number()
    city_value = fake.city()
    address_value = fake.address()
    email_value = fake.email()
    number_document_value = fake.ssn()
    date_birthday_value = fake.date_of_birth(minimum_age=18, maximum_age=70)
    gender_value = random.choice(['Male', 'Female'])

    first_name_value = check_length(first_name_value, 30)
    last_name_value = check_length(last_name_value, 30)
    phone_number_value = check_length(phone_number_value, 30)
    city_value = check_length(city_value, 60)
    address_value = check_length(address_value, 60)
    email_value = check_length(email_value, 100)
    number_document_value = check_length(number_document_value, 30)
    gender_value = check_length(gender_value, 6)

    customer = Customer.objects.create(
        first_name=first_name_value,
        last_name=last_name_value,
        phone_number=phone_number_value,
        city=city_value,
        address=address_value,
        email=email_value,
        number_document=number_document_value,
        date_birthday=date_birthday_value,
        gender=gender_value
    )

    # Для Employee
    appointment_value = random.choice(['Pawn Broker', 'Manager', 'Clerk', 'Salesperson'])
    first_name_value = fake.first_name()
    last_name_value = fake.last_name()
    phone_number_value = fake.phone_number()
    city_value = fake.city()
    address_value = fake.address()
    email_value = fake.email()
    password_value = fake.password()

    appointment_value = check_length(appointment_value, 30)
    first_name_value = check_length(first_name_value, 30)
    last_name_value = check_length(last_name_value, 30)
    phone_number_value = check_length(phone_number_value, 30)
    city_value = check_length(city_value, 60)
    address_value = check_length(address_value, 60)
    email_value = check_length(email_value, 100)
    password_value = check_length(password_value, 1200)

    employee = Employee.objects.create(
        first_name=first_name_value,
        last_name=last_name_value,
        phone_number=phone_number_value,
        city=city_value,
        address=address_value,
        email=email_value,
        appointment=appointment_value,
        hire_date=fake.date_this_decade(),
        salary=round(random.uniform(3000, 8000), 2),
        password=password_value
    )

    # Для ItemCategory
    type_item_value = random.choice(item_categories)
    info_item_value = fake.sentence()

    type_item_value = check_length(type_item_value, 50)
    info_item_value = check_length(info_item_value, 255)

    item_category = ItemCategory.objects.create(
        type_item=type_item_value,
        info_item=info_item_value
    )

    # Для Item
    name_product_value = random.choice(['Ring', 'Watch', 'Laptop', 'Guitar', 'Drill', 'Smartphone', 'Chair', 'Painting'])
    info_product_value = fake.sentence()
    serial_number_value = fake.uuid4()
    brand_value = fake.company()
    model_value = fake.word()
    photo_link_value = fake.image_url()

    name_product_value = check_length(name_product_value, 50)
    info_product_value = check_length(info_product_value, 255)
    serial_number_value = check_length(serial_number_value, 50)
    brand_value = check_length(brand_value, 50)
    model_value = check_length(model_value, 50)
    photo_link_value = check_length(photo_link_value, 256)

    item = Item.objects.create(
        name_product=name_product_value,
        info_product=info_product_value,
        category=item_category,
        appraised_value=round(random.uniform(100, 2000), 2),
        serial_number=serial_number_value,
        production_date=fake.date_this_decade(),
        brand=brand_value,
        model=model_value,
        photo_link=photo_link_value
    )

    # Для Credit

    sum_loan_value = round(random.uniform(1000, 5000), 2)
    percent_rate_value = round(random.uniform(5.0, 20.0), 2)
    start_date_value = fake.date_this_year()
    end_date_value = fake.date_between(start_date=start_date_value)

    # Перевірка на валідність суми та процентної ставки
    if sum_loan_value <= 0:
        raise ValueError(f"Invalid loan sum: {sum_loan_value}")
    if percent_rate_value <= 0:
        raise ValueError(f"Invalid percent rate: {percent_rate_value}")

    # Перевірка на правильність дат
    if end_date_value < start_date_value:
        raise ValueError(f"End date {end_date_value} cannot be before start date {start_date_value}.")

    # Отримати випадковий item з бази
    item = Item.objects.order_by('?').first()

    credit = Credit.objects.create(
        item_id=item.item_id,  # Використовуємо фактичний item_id
        client=customer,
        sum_loan=sum_loan_value,
        percent_rate=percent_rate_value,
        start_date=start_date_value,
        end_date=end_date_value,
        loan_status=random.choice(['Active', 'Extinguished', 'Outstanding'])
    )

    # Для ItemPledge
    item_pledge = ItemPledge.objects.create(
        item=item,
        pledge_date=fake.date_this_year(),
        condition_pledge=random.choice(['Good', 'Fair', 'Poor']),
        estimated_value=round(random.uniform(100, 1000), 2),
        loan_id=credit.credit_id
    )

    # Для Payment
    payment = Payment.objects.create(
        payment_credit=credit,
        date_payment_give=fake.date_this_year(),
        date_payment_return=fake.date_this_year(),
        sum_payment_give=round(random.uniform(100, 500), 2),
        way_payment_give=random.choice(['Cash', 'Card']),
        sum_payment_return=round(random.uniform(0, 500), 2),
        way_payment_return=random.choice(['Cash', 'Card']),
        employee_give=employee,
        employee_return=employee
    )

    # Для RatedItem
    rated_item = RatedItem.objects.create(
        item=item,
        rating_value=round(random.uniform(1.0, 5.0), 2),
        date_rating=fake.date_this_year(),
        employee=employee,
        description_item=fake.sentence()
    )

    # Для SoldItem
    sold_item = SoldItem.objects.create(
        item=item,
        date_sell=fake.date_this_year(),
        price_sell=round(random.uniform(100, 5000), 2),
        user_pledge=customer,
        employee=employee,
        other_user_id=random.randint(1, 100)
    )

    transaction_types = ['Cash', 'Card', 'Crypto']  # Правильні типи транзакцій

    amount_value = round(random.uniform(100, 5000), 2)  # Сума транзакції з округленням

    # Перевірка на валідність суми
    if amount_value <= 0:
        raise ValueError(f"Invalid amount for transaction: {amount_value}")

    # Вибір активного кредиту, якщо транзакція має бути пов'язана з кредитом
    active_credit = Credit.objects.filter(loan_status='Active').order_by('?').first() if random.choice(
        [True, False]) else None

    # Створення запису в TransactionPayment
    transaction_payment = TransactionPayment.objects.create(
        type_transaction=random.choice(transaction_types),  # Вибір правильного типу транзакції
        amount=amount_value,
        date_trans=fake.date_this_year(),
        credit=active_credit,
        employee=employee
    )

    print(f"TransactionPayment created with type: {transaction_payment.type_transaction}, amount: {amount_value}")

    # Для Inventory
    inventory = Inventory.objects.create(
        item=item,  # Вказуємо зв'язок з товаром
        status_item=random.choice(['In Stock', 'Sold', 'Pawned']),  # Вибір статусу товару
        date_inventory=fake.date_this_year()  # Вказуємо дату інвентаризації
    )

    # Для Report
    report = Report.objects.create(
        employee=employee,
        date_report=fake.date_this_year(),
        total_amount_transactions=round(random.uniform(1000, 5000), 2),  # Сума всіх транзакцій
        amount_pledge_sum=round(random.uniform(1000, 5000), 2),  # Сума всіх застав
        amount_sold_item_sum=round(random.uniform(1000, 5000), 2),  # Сума проданих товарів
        amount_pledge=random.randint(1, 10),  # Кількість застав
        amount_sold_item=random.randint(1, 10)  # Кількість проданих товарів
    )
