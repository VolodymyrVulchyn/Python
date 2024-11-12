from django.db import models
from django.contrib.auth.models import User

class Credit(models.Model):
    credit_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField(unique=True, blank=True, null=True)
    client = models.ForeignKey('Customer', models.DO_NOTHING, blank=True, null=True)
    sum_loan = models.DecimalField(max_digits=12, decimal_places=2)
    percent_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    loan_status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit'

    def _str__(self):
        return self.credit_id + ' | ' + self.client


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    city = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    number_document = models.CharField(max_length=30)
    date_birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True)
    password = models.CharField(max_length=1200, blank=True)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    appointment = models.CharField(max_length=30)
    hire_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    password = models.CharField(max_length=1200, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' | ' + self.appointment

    class Meta:
        managed = False
        db_table = 'employee'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)
    status_item = models.CharField(max_length=20, blank=True, null=True)
    date_inventory = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'

    def __str__(self):
        return self.inventory_id + ' | ' + self.item


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=50)
    info_product = models.CharField(max_length=256)
    category = models.ForeignKey('ItemCategory', models.DO_NOTHING)
    appraised_value = models.DecimalField(max_digits=10, decimal_places=2)
    serial_number = models.CharField(unique=True, max_length=50)
    production_date = models.DateField(blank=True, null=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    photo_link = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return str(self.item_id) + ' | ' + self.name_product


class ItemCategory(models.Model):
    type_item = models.CharField(max_length=50)
    info_item = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_category'

    def __str__(self):
        return self.type_item


class ItemPledge(models.Model):
    pledge_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    pledge_date = models.DateField()
    condition_pledge = models.CharField(max_length=20, blank=True, null=True)
    estimated_value = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    loan_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_pledge'

    def __str__(self):
        return self.pledge_id + ' | ' + self.item


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_credit = models.ForeignKey(Credit, models.DO_NOTHING)
    date_payment_give = models.DateField()
    date_payment_return = models.DateField(blank=True, null=True)
    sum_payment_give = models.DecimalField(max_digits=10, decimal_places=2)
    way_payment_give = models.CharField(max_length=30)
    sum_payment_return = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    way_payment_return = models.CharField(max_length=39, blank=True, null=True)
    employee_give = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    employee_return = models.ForeignKey(Employee, models.DO_NOTHING, related_name='payment_employee_return_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'

    def __str__(self):
        return self.payment_id + ' | ' + self.payment_credit


class RatedItem(models.Model):
    rate_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    rating_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_rating = models.DateField()
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    description_item = models.TextField()

    def __str__(self):
        return self.rate_id + ' | ' + self.item

    class Meta:
        managed = False
        db_table = 'rated_item'


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    date_report = models.DateField()
    total_amount_transactions = models.DecimalField(max_digits=13, decimal_places=2)
    amount_pledge_sum = models.DecimalField(max_digits=13, decimal_places=2)
    amount_sold_item_sum = models.DecimalField(max_digits=13, decimal_places=2)
    amount_pledge = models.IntegerField(blank=True, null=True)
    amount_sold_item = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'

    def __str__(self):
        return self.report_id + ' | ' + self.employee


class SoldItem(models.Model):
    sell_id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, models.DO_NOTHING)
    date_sell = models.DateField()
    price_sell = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    user_pledge = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    other_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sold_item'

    def __str__(self):
        return self.sell_id + ' | ' + self.item

class TransactionPayment(models.Model):
    trans_id = models.AutoField(primary_key=True)
    type_transaction = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_trans = models.DateField(blank=True, null=True)
    credit = models.ForeignKey(Credit, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_payment'

    def __str__(self):
        return self.trans_id + ' | ' + self.type_transaction
