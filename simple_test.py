
import logging

from portfolio import Portfolio
from security_object import SecurityObject
from trade_enum import TradeAction

logger = logging.getLogger(__name__)


total_portfolio_amount = 100_000

security1 = SecurityObject("IBM", 20, 10, -10, 150, total_portfolio_amount)
security2 = SecurityObject("MSFT", 20, 20, 0, 90, total_portfolio_amount)
security3 = SecurityObject("ORCL", 20, 30, 10, 220, total_portfolio_amount)
security4 = SecurityObject("AAPL", 20, 20, 0, 450, total_portfolio_amount)
security5 = SecurityObject("HD", 20, 20, 0, 70, total_portfolio_amount)

securities = [security1, security2, security3, security4, security5]

my_portfolio = Portfolio(total_portfolio_amount, securities)

securities_to_sell = []
securities_to_buy = []

for security in securities:
    action = security.determine_trade_action()

    if action is not None:
        total_trade_amount, shares_traded = security.trade_shares(action)
        logger.info(f"Security {security.security} was traded. Action: {action}, "
                    f"Total Trade Amount: ${total_trade_amount}, Shares Traded: {shares_traded}")

        if action == TradeAction.SELL:
            my_portfolio.top_up_cash(total_trade_amount)
        elif action == TradeAction.BUY:
            my_portfolio.withdraw_cash(total_trade_amount)
    else:
        logger.error(f"Invalid action returned for security: {security.security}. Action: {action}")
        break

print(f"Final free cash in portfolio: ${my_portfolio.free_cash}")
print(f"Final portfolio amount: ${my_portfolio.get_total_portfolio_value()}")

for security in my_portfolio.securities:
    print(f"{security}")

# buy securities
