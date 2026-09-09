
from dataclasses import dataclass

@dataclass
class SecurityObject:
    security: str
    target: float
    current: float
    target_variance: float
    unit_price: float

    def stock_value_in_usd(self):
        pass


    def calculate_investment(self, total_amount):
        """
        Calculate the total investment for this security.

        :param total_amount: Total investment amount
        :return: Total investment for this security
        """
        investment_amount_usd = total_amount * self.current_allocation / 100
        investment_amount_stocks = investment_amount_usd / self.unit_price
        return investment_amount_usd, investment_amount_stocks


