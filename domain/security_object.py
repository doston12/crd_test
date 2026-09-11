
import logging
from domain.trade_enum import TradeAction

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)
logger = logging.getLogger(__name__)


class SecurityObject:

    def __init__(self, security, target, current, target_variance, unit_price, total_portfolio_amount):
        # later, add method to check for data validation for each field.

        self.security = security
        self.target = target
        self.current = current
        self.target_variance = target_variance
        self.unit_price = unit_price
        self.total_portfolio_amount = total_portfolio_amount

        # later add methods to check for data validation...
        self.portfolio_amount = total_portfolio_amount * self.current / 100

    def get_available_shares(self):
        """
        Calculate the number of shares available for this security, considering the portfolio amount for this security

        :return: Number of shares available
        """
        # later add methods to check for data validation...
        return self.portfolio_amount / self.unit_price

    def determine_trade_action(self):
        """
        Determine whether to buy or sell shares based on the current allocation and target allocation.

        :return: TradeAction Enum (BUY or SELL)
        """
        if self.target_variance > 0:
            return TradeAction.SELL
        elif self.target_variance < 0:
            return TradeAction.BUY
        elif self.target_variance == 0:
            return TradeAction.NO_ACTION_REQUIRED

        else:
            logger.error(f"Something went wrong. Invalid state for security: {self.security}")
            return None

    def trade_shares(self, action):
        if action == TradeAction.SELL or action == TradeAction.BUY:
            total_trade_amount = self.total_portfolio_amount * abs(self.target_variance) / 100
            shares_traded = total_trade_amount / self.unit_price
            logger.info(
                f"Calculated {action.value} of {shares_traded} shares of "
                f"{self.security} for ${total_trade_amount}"
            )

            if action == TradeAction.SELL:
                self.portfolio_amount -= total_trade_amount
            elif action == TradeAction.BUY:
                self.portfolio_amount += total_trade_amount

            self.current = self.portfolio_amount / self.total_portfolio_amount * 100
            self.reset_target_variance(self.current - self.target)

            return total_trade_amount, shares_traded, self.portfolio_amount

        elif action == TradeAction.NO_ACTION_REQUIRED:
            logger.info(f"No action required for security: {self.security}")
            return 0, 0, self.portfolio_amount

        else:
            logger.error(f"Invalid trade action for security: {self.security}, got action: {action}")
            return None

    def reset_target_variance(self, new_target_variance):
        """
        Reset the target variance for this security.

        :param new_target_variance: New target variance value
        """
        logger.info(f"Reset target variance for security: {self.security} to {new_target_variance}")
        self.target_variance = new_target_variance

    def __repr__(self):
        return (f"SecurityObject(security={self.security}, target={self.target}, "
                f"current={self.current}, target_variance={self.target_variance}, "
                f"unit_price={self.unit_price}, portfolio_amount={self.portfolio_amount})")
