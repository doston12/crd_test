
import logging

logger = logging.getLogger(__name__)


class Portfolio:

    def __init__(self, total_amount, securities):
        # later add data validation checks...
        self.total_amount = total_amount
        self.securities = securities

        # to represent, the amount of cash we have available to invest in the portfolio.
        # This will be used to determine how much we can buy/sell for each security.
        self.free_cash = 0

    def top_up_cash(self, amount):
        """
        Add cash to the portfolio's free cash.

        :param amount: Amount of cash to add
        """
        self.free_cash += amount
        logger.info(f"Topped up cash by ${amount}. Total free cash: ${self.free_cash}")

    def withdraw_cash(self, amount):
        """
        Withdraw cash from the portfolio's free cash.

        :param amount: Amount of cash to withdraw
        """
        if amount > self.free_cash:
            logger.error(f"Insufficient free cash to withdraw ${amount}. Available: ${self.free_cash}")
            return False

        self.free_cash -= amount
        logger.info(f"Withdrew ${amount}. Total free cash: ${self.free_cash}")
        return True

    def get_total_portfolio_value(self):
        """
        Calculate the total value of the portfolio, including free cash and the value of all securities.

        :return: Total portfolio value
        """
        total_value = self.free_cash
        for security in self.securities:
            total_value += security.get_available_shares() * security.unit_price
        return total_value
