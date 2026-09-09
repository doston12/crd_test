

from trade_enum import TradeAction


class SecurityObject:

    def __init__(self, security, target, current, target_variance, unit_price, total_portfolio_amount):
        # later, add method to check for data validation for each field.

        self.security = security
        self.target = target
        self.current = current
        self.target_variance = target_variance
        self.unit_price = unit_price

        # later add methods to check for data validation...
        self.portfolio_amount = total_portfolio_amount * self.current / 100

    def calculate_shares_available(self):
        """
        Calculate the number of shares available for this security, considering the portfolio amount for this security

        :return: Number of shares available
        """
        # later add methods to check for data validation...
        return self.portfolio_amount / self.unit_price

    def trade_shares(self, action):
        if action == TradeAction.SELL:
            pass

        if action == TradeAction.BUY:
            pass



