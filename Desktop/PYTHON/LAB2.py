class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self._condition = "Good"

    @property
    def condition(self):
        return self._condition

    def display_info(self):
        print(f"Item: {self.name}, Value: {self.value}, Condition: {self._condition}")

    def update_value(self, new_value):
        self.value = new_value
        print(f"Updated value of {self.name}: {self.value}")

    @staticmethod
    def calculate_interest(value, rate=0.10):
        interest = value * rate
        print(f"Interest on {value} with rate {rate}: {interest}")
        return interest

class Warranty:
    def __init__(self, warranty_period):
        self.warranty_period = warranty_period

    def display_warranty(self):
        print(f"Warranty period: {self.warranty_period} months")

class Jewelry(Item, Warranty):
    def __init__(self, name, value, metal_type, warranty_period):
        Item.__init__(self, name, value)
        Warranty.__init__(self, warranty_period)
        self.metal_type = metal_type

    def display_info(self):
        super().display_info()
        print(f"Metal Type: {self.metal_type}")
        self.display_warranty()

class Electronics(Item, Warranty):
    def __init__(self, name, value, brand, warranty_period):
        Item.__init__(self, name, value)
        Warranty.__init__(self, warranty_period)
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        self.display_warranty()

class User:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def display_user_info(self):
        print(f"User: {self.name}, Balance: {self._balance}")

    def update_balance(self, amount):
        self._balance += amount
        print(f"Updated balance for {self.name}: {self._balance}")

class VIPUser(User):
    def __init__(self, name, balance, vip_discount):
        super().__init__(name, balance)
        self.vip_discount = vip_discount

    def display_user_info(self):
        super().display_user_info()
        print(f"VIP Discount: {self.vip_discount}%")

    def apply_vip_discount(self, item_value):
        discounted_value = item_value * (1 - self.vip_discount / 100)
        print(f"Original item value: {item_value}, Discounted value: {discounted_value}")
        return discounted_value


def display():

    ring = Jewelry("Gold Ring", 5000, "Gold", 12)
    phone = Electronics("Smartphone", 20000, "Apple", 24)
    user = User("Alfredo Bambolino", 15000)
    vip_user = VIPUser("Tarakan Oleg", 50000, 10)

    print("\nUser Info:")
    user.display_user_info()

    print("\nVIP User Info:")
    vip_user.display_user_info()

    print("\nApplying VIP discount for ring:")
    vip_price = vip_user.apply_vip_discount(ring.value)

    print("\nUpdating user balance after buying the ring:")
    vip_user.update_balance(-vip_price)

    print("\nUpdated VIP User Info:")
    vip_user.display_user_info()

    print("\nJewelry (Ring) Info:")
    ring.display_info()

    print("\nElectronics (Phone) Info:")
    phone.display_info()

    print("\nUpdating values...")
    ring.update_value(5200)
    phone.update_value(18000)

    print("\nUpdated Jewelry (Ring) Info:")
    ring.display_info()

    print("\nUpdated Electronics (Phone) Info:")
    phone.display_info()

    print("\nCalculating interest:")
    interest_ring = Item.calculate_interest(ring.value)
    interest_phone = Item.calculate_interest(phone.value)

display()
