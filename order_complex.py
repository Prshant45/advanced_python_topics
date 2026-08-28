from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Type


# --- DOMAIN ENTITIES ---

@dataclass(frozen=True)
class Order:
    order_id: str
    amount: float


# --- ABSTRACT PRODUCTS ---

class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self) -> str:
        pass


class PaymentAggregator(ABC):
    def __init__(self, name: str, fee_percentage: float):
        self.name = name
        self.fee_percentage = fee_percentage

    @abstractmethod
    def process_charge(self, order: Order, method: PaymentMethod) -> bool:
        pass


# --- CONCRETE PRODUCTS (STRIPE ECOSYSTEM) ---

class StripeAggregator(PaymentAggregator):
    def __init__(self):
        super().__init__(name="Stripe Gateway", fee_percentage=2.9)

    def process_charge(self, order: Order, method: PaymentMethod) -> bool:
        print(f"[{self.name}] Charging ${order.amount:.2f} for Order #{order.order_id}")
        print(f"[{self.name}] Routing via {method.get_details()}")
        return True


class StripeCardPayment(PaymentMethod):
    def __init__(self, token: str):
        self.token = token

    def get_details(self) -> str:
        return f"Stripe Card Token ({self.token})"


class StripeUPIPayment(PaymentMethod):
    def __init__(self, vpa: str):
        self.vpa = vpa

    def get_details(self) -> str:
        return f"Stripe UPI Intent ({self.vpa})"


# --- CONCRETE PRODUCTS (RAZORPAY ECOSYSTEM) ---

class RazorpayAggregator(PaymentAggregator):
    def __init__(self):
        super().__init__(name="Razorpay Gateway", fee_percentage=2.0)

    def process_charge(self, order: Order, method: PaymentMethod) -> bool:
        print(f"[{self.name}] Capturing ₹{order.amount:.2f} for Order #{order.order_id}")
        print(f"[{self.name}] Routing via {method.get_details()}")
        return True


class RazorpayCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.last4 = card_number[-4:]

    def get_details(self) -> str:
        return f"Razorpay Card Vault (ending {self.last4})"


class RazorpayUPIPayment(PaymentMethod):
    def __init__(self, vpa: str):
        self.vpa = vpa

    def get_details(self) -> str:
        return f"Razorpay UPI Handle ({self.vpa})"


# --- ABSTRACT FACTORY ---

class PaymentGatewayFactory(ABC):
    """Abstract Factory interface defining the family of products for any gateway."""

    @abstractmethod
    def get_aggregator(self) -> PaymentAggregator:
        pass

    @abstractmethod
    def create_card_payment(self) -> PaymentMethod:
        pass

    @abstractmethod
    def create_upi_payment(self) -> PaymentMethod:
        pass


# --- CONCRETE FACTORIES ---

class StripeGatewayFactory(PaymentGatewayFactory):
    def get_aggregator(self) -> PaymentAggregator:
        return StripeAggregator()

    def create_card_payment(self) -> PaymentMethod:
        card = input("Enter Card Number: ").strip() or "4242"
        return StripeCardPayment(token=f"tok_{card[-4:]}")

    def create_upi_payment(self) -> PaymentMethod:
        upi_id = input("Enter UPI ID: ").strip() or "user@okstripe"
        return StripeUPIPayment(vpa=upi_id)


class RazorpayGatewayFactory(PaymentGatewayFactory):
    def get_aggregator(self) -> PaymentAggregator:
        return RazorpayAggregator()

    def create_card_payment(self) -> PaymentMethod:
        card = input("Enter Card Number: ").strip() or "5521"
        return RazorpayCardPayment(card_number=card)

    def create_upi_payment(self) -> PaymentMethod:
        upi_id = input("Enter UPI ID: ").strip() or "user@okaxis"
        return RazorpayUPIPayment(vpa=upi_id)


# --- CHECKOUT CLI WORKFLOW ---

class CheckoutEngine:
    _factories: Dict[str, Type[PaymentGatewayFactory]] = {
        "1": StripeGatewayFactory,
        "2": RazorpayGatewayFactory,
    }

    @classmethod
    def run(cls, order: Order) -> None:
        print("Select Gateway:")
        print("1. Stripe")
        print("2. Razorpay")
        gateway_choice = input("Option (1-2): ").strip()

        factory_cls = cls._factories.get(gateway_choice)
        if not factory_cls:
            print("Invalid gateway.")
            return

        factory = factory_cls()
        aggregator = factory.get_aggregator()

        print("\nSelect Payment Method:")
        print("1. Credit/Debit Card")
        print("2. UPI")
        method_choice = input("Option (1-2): ").strip()

        if method_choice == "1":
            method = factory.create_card_payment()
        elif method_choice == "2":
            method = factory.create_upi_payment()
        else:
            print("Invalid payment method.")
            return

        print()
        aggregator.process_charge(order, method)


if __name__ == "__main__":
    current_order = Order(order_id="ORD-4402", amount=89.99)
    CheckoutEngine.run(current_order)
