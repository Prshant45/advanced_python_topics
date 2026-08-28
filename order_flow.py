from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List, Type


# --- CORE DOMAIN MODELS ---

@dataclass(frozen=True)
class OrderItem:
    name: str
    price: float
    qty: int

    @property
    def total(self) -> float:
        return self.price * self.qty


class Order:
    __slots__ = ("order_id", "items")

    def __init__(self, order_id: str, items: List[OrderItem]):
        self.order_id = order_id
        self.items = items

    @property
    def amount(self) -> float:
        return sum(item.total for item in self.items)


# --- PAYMENT METHOD INTERFACE & IMPLEMENTATIONS ---

class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self) -> str:
        pass


class UPIPayment(PaymentMethod):
    def __init__(self, vpa: str):
        self.vpa = vpa

    def get_details(self) -> str:
        return f"UPI ({self.vpa})"


class CardPayment(PaymentMethod):
    def __init__(self, last4: str):
        self.last4 = last4

    def get_details(self) -> str:
        return f"Card ending in {self.last4}"


# --- AGGREGATOR INTERFACE (ABC) ---

class BasePaymentAggregator(ABC):
    """Common blueprint for all payment aggregators/gateways."""
    
    def __init__(self, name: str, fee_percentage: float):
        self.name = name
        self.fee_percentage = fee_percentage

    def calculate_processing_fee(self, amount: float) -> float:
        return (amount * self.fee_percentage) / 100

    @abstractmethod
    def process_charge(self, order_id: str, amount: float, method: PaymentMethod) -> bool:
        """Each aggregator implements its specific API charge logic."""
        pass


# --- CONCRETE AGGREGATOR IMPLEMENTATIONS ---

class StripeAggregator(BasePaymentAggregator):
    def __init__(self):
        super().__init__(name="Stripe Gateway", fee_percentage=2.9)

    def process_charge(self, order_id: str, amount: float, method: PaymentMethod) -> bool:
        fee = self.calculate_processing_fee(amount)
        print(f"[{self.name}] Creating Stripe ChargeIntent for Order: {order_id}")
        print(f"[{self.name}] Routing via {method.get_details()} | Total: ${amount:.2f} (Platform Fee: ${fee:.2f})")
        print(f"[{self.name}] Charge verified successfully.")
        return True


class RazorpayAggregator(BasePaymentAggregator):
    def __init__(self):
        super().__init__(name="Razorpay Gateway", fee_percentage=2.0)

    def process_charge(self, order_id: str, amount: float, method: PaymentMethod) -> bool:
        fee = self.calculate_processing_fee(amount)
        print(f"[{self.name}] Generating Razorpay Payment Order for: {order_id}")
        print(f"[{self.name}] Captured via {method.get_details()} | Total: ₹{amount:.2f} (Platform Fee: ₹{fee:.2f})")
        print(f"[{self.name}] Payment captured successfully.")
        return True


class PayPalAggregator(BasePaymentAggregator):
    def __init__(self):
        super().__init__(name="PayPal Gateway", fee_percentage=3.49)

    def process_charge(self, order_id: str, amount: float, method: PaymentMethod) -> bool:
        fee = self.calculate_processing_fee(amount)
        print(f"[{self.name}] Directing to PayPal Express Checkout for: {order_id}")
        print(f"[{self.name}] Method: {method.get_details()} | Total: ${amount:.2f} (Platform Fee: ${fee:.2f})")
        print(f"[{self.name}] Token executed successfully.")
        return True


# --- AGGREGATOR FACTORY ---

class AggregatorFactory:
    """Registry-based factory for dynamically resolving aggregators."""
    
    _registry: Dict[str, Type[BasePaymentAggregator]] = {
        "1": StripeAggregator,
        "2": RazorpayAggregator,
        "3": PayPalAggregator,
    }

    @classmethod
    def get_aggregator(cls, choice: str) -> BasePaymentAggregator:
        aggregator_cls = cls._registry.get(choice)
        if not aggregator_cls:
            raise ValueError("Unsupported aggregator selected.")
        return aggregator_cls()


# --- CLI WORKFLOW ---

def run_checkout():
    order = Order("ORD-8832", [OrderItem("Pro Keyboard", 150.0, 1), OrderItem("Mousepad", 20.0, 1)])
    print(f"Order #{order.order_id} total: ${order.amount:.2f}\n")

    print("Choose Payment Aggregator:")
    print("1. Stripe (Global Cards/UPI)")
    print("2. Razorpay (India & UPI Optimized)")
    print("3. PayPal (International)")
    agg_choice = input("Select Gateway (1-3): ").strip()

    print("\nChoose Payment Method:")
    print("1. Card")
    print("2. UPI")
    method_choice = input("Select Method (1-2): ").strip()

    method: PaymentMethod
    if method_choice == "1":
        method = CardPayment("4242")
    elif method_choice == "2":
        method = UPIPayment("buyer@bank")
    else:
        print("Invalid payment method.")
        return

    # Dynamic dispatch through factory
    try:
        aggregator = AggregatorFactory.get_aggregator(agg_choice)
        aggregator.process_charge(order.order_id, order.amount, method)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    run_checkout()
