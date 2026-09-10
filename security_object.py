
import logging
from trade_enum import TradeAction


logger = logging.getLogger(__name__)


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
            logger.info(f"Trading {abs(self.target_variance)} shares of security: {self.security}")
            total_trade_amount = self.portfolio_amount * abs(self.target_variance) / 100
            shares_to_trade = total_trade_amount / self.unit_price
            self.reset_target_variance(0)
            return total_trade_amount, shares_to_trade

        elif action == TradeAction.NO_ACTION_REQUIRED:
            logger.info(f"No action required for security: {self.security}")
            return 0, 0

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