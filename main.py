import logging

# testing: consider floating point numbers, 66.66666666666667, how many digits we want to keep after the .
# test whether given security names are valid, they should be public companies
# test that given inputs correct, i.e target variance = target - current. What if we have written 100 in one of the test file, or zero


TOTAL_AMOUNT = 100_000
TOTAL_SHARES = 5
SECURITY = ['IBM', 'MSFT', 'ORCL', 'AAPL', 'HD']
TARGET = [20, 20, 20, 20, 20]
CURRENT = [10, 20, 30, 20, 20]
TARGET_VARIANCE = [-10, 0, 10, 0, 0]
UNIT_PRICE = [150, 90, 220, 450, 70]

logger = logging.getLogger(__name__)


def rebalance_portfolio(n=TOTAL_SHARES, target=TARGET, current=CURRENT, target_variance=TARGET_VARIANCE, unit_price=UNIT_PRICE):
    """
    Rebalance the portfolio to match the target allocation.

    :param n: Total number of shares
    :param target: Target allocation
    :param current: Current allocation
    :param target_variance: Target variance
    :param unit_price: Unit price of each share
    :return: List of shares to buy/sell for each stock
    """
    pass


def return_investment_for_each_security(n=TOTAL_SHARES, current=CURRENT, unit_price=UNIT_PRICE):
    """
    Calculate the total investment for each security.

    :param n: Total number of shares
    :param current: Current allocation
    :param unit_price: Unit price of each share
    :return: List of total investment for each security
    """
    global TOTAL_AMOUNT
    investment_amount_usd = []
    investment_amount_stocks = []

    for i in range(n):
        amount = TOTAL_AMOUNT * current[i] / 100
        investment_amount_usd.append(amount)
        investment_amount_stocks.append(amount / unit_price[i])

    return investment_amount_usd, investment_amount_stocks


# def calculate_investment_for_security(current, unit_price):
#     """
#     Calculate the total investment for a specific security.
#
#     :param security_name: Name of the security
#     :param current: Current allocation
#     :param unit_price: Unit price of each share
#     :return: Total investment for the specified security
#     """
#     if security_name not in SECURITY:
#         logger.error(f"Security {security_name} not found in the portfolio.")
#         return None
#
#     amount = TOTAL_AMOUNT * current[] / 100
#     investment_amount_stock = amount / unit_price[index]
#
#     return amount, investment_amount_stock


def determine_how_much_to_sell_or_buy(n=TOTAL_SHARES, current=CURRENT, target=TARGET, target_variance=TARGET_VARIANCE, unit_price=UNIT_PRICE):
    """
    Determine how much to sell or buy for each security.

    :param n: Total number of shares
    :param current: Current allocation
    :param target: Target allocation
    :param target_variance: Target variance
    :param unit_price: Unit price of each share
    :return: List of shares to buy/sell for each stock
    """
    if not check_is_target_variance_valid(n, target, current, target_variance):
        logger.warning("Target variance is invalid. Please check the inputs.")
        return None

    investment_amount_usd, investment_amount_stock = calculate_investment_for_security(TOTAL_SHARES, CURRENT, UNIT_PRICE)

    for i in range(n):
        # sell
        if target_variance[i] > 0:
            logger.info(f"Buy {target_variance[i]} shares of {SECURITY[i]}")
            amount = sell_or_buy_shares(True, target_variance[i], unit_price[i])
        # buy
        elif target_variance[i] < 0:
            logger.info(f"Sell {abs(target_variance[i])} shares of {SECURITY[i]}")


def check_is_target_variance_valid(n=TOTAL_SHARES, target=TARGET, current=CURRENT, target_variance=TARGET_VARIANCE):
    """
    Check if the target variance is valid.

    :param n: Total number of shares
    :param target: Target allocation
    :param current: Current allocation
    :param target_variance: Target variance
    :return: True if valid, False otherwise
    """
    for i in range(n):
        if target[i] - current[i] != target_variance[i]:
            logger.error(f"Target variance is invalid for security {SECURITY[i]}: target - current = {target[i] - current[i]}, but target_variance = {target_variance[i]}")
            return False
    return True


def sell_or_buy_shares(sell_or_buy, target_variance, unit_price):
    """
    Sell or buy shares based on the target variance.

    :param target_variance: Target variance
    :return: None
    """

    if not isinstance(sell_or_buy, bool):
        logger.error(f"Invalid input for sell_or_buy: {sell_or_buy}. Must be a boolean.")
        return None

    # if True sell
    if sell_or_buy:
        return target_variance * unit_price

    # if False buy
    else:
        pass


def transaction_operation(sell_or_buy, target_variance, unit_price):
    # the purpose of this is to imitate that real $$$ transactions happen in special methods,
    # which support rolling back safely if something goes wong. Like, SQL procedures

    if not isinstance(sell_or_buy, bool):
        logger.error(f"Invalid input for sell_or_buy: {sell_or_buy}. Must be a boolean.")
        return None

    # investment_amount_usd, investment_amount_stock = return_investment_for_each_security(TOTAL_SHARES, CURRENT, UNIT_PRICE)

    # if True sell
    if sell_or_buy:
        return

    # if False buy
    else:
        pass


if __name__ == '__main__':
    print(return_investment_for_each_security())

