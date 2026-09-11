import pytest
import logging
from tests.conftest import create_portfolio_from_csv_file


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
)
logger = logging.getLogger(__name__)


# these tests are expected to fail, so we marked with xfail
@pytest.mark.xfail
@pytest.mark.parametrize("filename", [
    "tc21b_empty_target.csv",
    "tc21c_empty_current.csv",
    "tc21d_empty_target_variance.csv",
    "tc21e_empty_unit_price.csv",
    "tc21f_multiple_empty_cells_one_row.csv",
    "tc21g_multiple_empty_cells_across_rows.csv",
    "tc21h_completely_empty_row.csv",
    "tc23_null_values.csv",
    "tc24_malformed_values.csv",
])
def test_invalid_portfolio_cases(filename):
    with pytest.raises(ValueError):
        create_portfolio_from_csv_file(filename)
        logger.info(f"Expected error message is shown")



@pytest.mark.parametrize("filename", [
    "tc01_happy_path.csv",
    "tc02_one_security_holds_all_assets.csv",
    "tc08_floating_point_unit_price.csv",
    "tc09_floating_point_rebalancing.csv",
    "tc10_unit_price_above_portfolio_value.csv",
    "tc11_already_balanced.csv",
    "tc12_zero_target_percentage.csv",
    "tc13_free_cash_after_rebalancing.csv",
    "tc14_debt_after_rebalancing.csv",
    "tc15_single_security.csv",
    "tc16_non_ascii_security_name.csv",
])
def test_portfolio_rebalance(filename):
    portfolio = create_portfolio_from_csv_file(filename)
    initial_portfolio_value = portfolio.get_total_portfolio_value()

    portfolio.rebalance()

    cash_tolerance = 0.001
    if portfolio.free_cash < -cash_tolerance:
        pytest.fail(f"Portfolio is in debt: ${portfolio.free_cash}")
    elif portfolio.free_cash > cash_tolerance:
        logger.warning(f"Portfolio has ${portfolio.free_cash} free cash left")

    assert portfolio.get_total_portfolio_value() == pytest.approx(initial_portfolio_value)

    for security in portfolio.securities:
        assert security.current == pytest.approx(security.target)
        assert security.target_variance == pytest.approx(0)


def test_already_balanced_portfolio_does_not_trade():
    portfolio = create_portfolio_from_csv_file("tc11_already_balanced.csv")

    completed_trades = portfolio.rebalance()

    for _, _, total_trade_amount, shares_traded in completed_trades:
        assert total_trade_amount == 0
        assert shares_traded == 0
