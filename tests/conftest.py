
import pytest
import csv

from pathlib import Path

from domain.portfolio import Portfolio
from domain.security_object import SecurityObject

# we could declare these constants in some env file or configuration properties file. For simplicity keep it here
TOTAL_PORTFOLIO_AMOUNT = 100_000
CSV_DIR = Path(__file__).parent / "test_data"

@pytest.fixture
def total_portfolio_amount():
    return TOTAL_PORTFOLIO_AMOUNT


def read_csv_file(filename):
    """"Read csv file and return a dictionary from csv rows"""
    csv_path = CSV_DIR / filename
    with csv_path.open(mode="r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def create_portfolio_from_csv_file(filename):
    csv_test_data = read_csv_file(filename)
    securities = []

    for row in csv_test_data:
        security = SecurityObject(
            security=row["security"],
            target=float(row["target"]),
            current=float(row["current"]),
            target_variance=float(row["target_variance"]),
            unit_price=float(row["unit_price"]),
            total_portfolio_amount=TOTAL_PORTFOLIO_AMOUNT,

        )
        securities.append(security)

    return Portfolio(TOTAL_PORTFOLIO_AMOUNT, securities=securities)

