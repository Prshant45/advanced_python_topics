# get order calculator the total and use payment method to pay.
# method to pay -  card, upi

import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict


# __init__ - constructor
# __str__ - string representation of the object
@dataclass
class Item:
    name: str
    price: float
    quantity: int


class Order:
    # Order([item1, item2, ...])
    # self - current instance of the class
    # instance variable - self.items
    # class variable - Order.items
    # class method - @classmethod
    # instance method - def method(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Order':
        items = [Item(**item) for item in data['items']]
        return cls(items)

    # ord1 == ord2
    # ord1 = Order(1)
    # ord2 = ord1
    # ord1 == ord2 -> true
    # ord2 = Order(1)
    # ord1 == ord2 -> false
    def __init__(self, order_id, items: List[Item]):
        self.order_id = order_id
        self.items = items

    @property
    def total_items(self) -> int:
        return sum(item.quantity for item in self.items)

    # ord1.grand_total = 1000 ---- X
    # ord1.grand_total 
    # readbale variable # abstraction
    @property
    def grand_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

class PaymentMethod(ABC):

    @abstractmethod
    def get_payment_details(self):
        pass

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CardPayment(PaymentMethod): # inheritance

    def get_payment_details(self):
        print("Getting card payment details.")
        self.card_number = input("Enter card number: ")
        self.card_holder = input("Enter card holder name: ")
        self.expiry_date = input("Enter expiry date (MM/YY): ")

    def pay(self, amount: float) -> bool: # runtime polymorphism
        print(f"Paying {amount} using Card.")
        return True

class UpiPayment(PaymentMethod):

    def get_payment_details(self):
        print("Getting UPI payment details.")
        self.upi_id = input("Enter UPI ID: ")

    def pay(self, amount: float) -> bool:
        print(f"Paying {amount} using UPI.")
        return True
class WalletPayment(PaymentMethod):

    def get_payment_details(self):
        print("Getting Wallet payment details.")
        self.wallet_id = input("Enter Wallet ID: ")

    def pay(self, amount: float) -> bool:
        print(f"Paying {amount} using Wallet.")
        return True

#paymentmethod - parent - abstract class
# - get_details
# - pay
#rajorpayupipayment - child
#rajorpaycardpayment - child

#stripeupipayment - child
#stripecardpayment - child

# FactoryPaymentMethod - factory class abstract class
# - factory - dict
# - get_payment_object - class method
# rajorpayfactory - factory class
# stripefactory - factory class

# Aggerator - class - abstract class
# - call_get_payment_object method
# rajorpayaggerator - child
# - processing_fee - field
# stripeaggerator - child

# AggeratorFactory - factory class - concrete class
# - factory - dict
# - get_aggerator_object - class method

# method - upi/card - upi
# aggerator - stripe/rajorpay - stripe
# AggeratorFactory.get_aggerator_object -> stripeaggerator -> 
# stripefactory -> stripeupipayment





class PaymentMethodFactory:
    factory = {
        "1": CardPayment,
        "2": UpiPayment,
        "3": WalletPayment
    } # dictionary # class variable
    # dictionary # class variable

    @classmethod
    def get_payment_object(cls, choice: str) -> PaymentMethod:
        if choice in cls.factory:
            return cls.factory[choice]()
        raise ValueError(f"Unsupported payment method: {choice}")

class PaymentAggregator:
    def __init__(self):
        self.name = "Stripe Payment Aggregator"

    def process_payment(self, amount: float, payment_method: PaymentMethod) -> None:
        success = payment_method.pay(amount)
        if success:
           print(f"Payment of {amount} processed successfully.")
        else:
            print(f"Payment of {amount} failed.")

def process_order():
    items : List[Item] = []
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
            if not items:
                print("at least one item is required to place an order.")
                continue
        try:
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
        if price < 0 or quantity < 0:
            print("Price and quantity must be non-negative. Please try again.")
            continue
        items.append(Item(name, price, quantity))
    return items

def select_payment_method():
    print("Select a payment method:")
    print("1. Credit Card")
    print("2. UPI")
    print("3. Wallet")
    choice = input("Enter your choice (1, 2, or 3): ")
    payment_method = PaymentMethodFactory.get_payment_object(choice)
    payment_method.get_payment_details()
    return payment_method


def main():
    print("Welcome to the Order Processing System!")
    order_id = input("Enter order ID: ")
    items = process_order()
    if not items:
        print("No items were added to the order. Exiting.")
        sys.exit(1)
    order = Order(order_id, items)
    print(f"Total items: {order.total_items}")
    print(f"Grand total: {order.grand_total}")

    payment_method = select_payment_method()
    aggregator = PaymentAggregator()
    aggregator.process_payment(order.grand_total, payment_method)


if __name__ == "__main__":
    main()
