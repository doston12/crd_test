
import logging
from domain.trade_enum import TradeAction

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)
logger = logging.getLogger(__name__)


class Portfolio:

    def __init__(self, total_amount, securities):
        # later add data validation checks...
        self.total_amount = total_amount
        self.securities = securities

        # to represent, the amount of cash we have available to invest in the portfolio.
        # This will be used to determine how much we can buy/sell for each security.
        # invested_amount = sum(security.portfolio_amount for security in securities)
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
        self.free_cash -= amount
        logger.info(f"Withdrew ${amount}. Total free cash: ${self.free_cash}")

    def get_total_portfolio_value(self):
        """
        Calculate the total value of the portfolio, including free cash and the value of all securities.

        :return: Total portfolio value
        """
        invested_amount = sum(security.portfolio_amount for security in self.securities)
        return self.free_cash + invested_amount

    def rebalance(self):
        """Sell overweight securities first, then fund purchases."""
        actions = {}
        for security in self.securities:
            actions[security] = security.determine_trade_action()

        completed_trades = []
        for security, action in actions.items():

            total_trade_amount, shares_traded, total_security_amount = security.trade_shares(action)

            if any(
                    value is None
                    for value in (total_trade_amount, shares_traded, total_security_amount)
            ):
                logger.warning(f"Unexpected state: 'None' for security: {security.security}. Investigate logs")
                continue

            if action == TradeAction.SELL:
                self.top_up_cash(total_trade_amount)
            elif action == TradeAction.BUY:
                # Assumption: if we have to buy first, account goes negative and later when we sell,
                # we will have enough cash to buy. This is a simplification, avoided over-engineering..
                self.withdraw_cash(total_trade_amount)

            logger.info(
                f"Executed {action.value} for {security.security}: "
                f"${total_trade_amount}, {shares_traded} shares"
            )
            completed_trades.append((security, action, total_trade_amount, shares_traded))

        return completed_trades
