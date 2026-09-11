
import logging

from domain.portfolio import Portfolio
from domain.security_object import SecurityObject

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)
logger = logging.getLogger(__name__)


total_portfolio_amount = 100_000

security1 = SecurityObject("IBM", 20, 10, -10, 150, total_portfolio_amount)
security2 = SecurityObject("MSFT", 20, 20, 0, 90, total_portfolio_amount)
security3 = SecurityObject("ORCL", 20, 30, 10, 220, total_portfolio_amount)
security4 = SecurityObject("AAPL", 20, 20, 0, 450, total_portfolio_amount)
security5 = SecurityObject("HD", 20, 20, 0, 70, total_portfolio_amount)

securities = [security1, security2, security3, security4, security5]

my_portfolio = Portfolio(total_portfolio_amount, securities)

my_portfolio.rebalance()

logger.info("\nAfter rebalance:")
logger.info("Portfolio free cash: ${}".format(my_portfolio.free_cash))
for security in my_portfolio.securities:
    logger.info(f"{security}")
