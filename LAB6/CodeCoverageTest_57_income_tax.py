
import pytest
from income_tax import taxable_income, tax_due, refund_status


# TAXABLE INCOME TESTS

def test_new_regime():
    assert taxable_income(1000000, "new", 0) == 925000


def test_old_regime():
    assert taxable_income(1000000, "old", 100000) == 850000


def test_old_regime_investment_limit():
    assert taxable_income(1000000, "old", 200000) == 800000


def test_negative_gross_income():
    with pytest.raises(ValueError):
        taxable_income(-1000, "new", 0)


def test_unknown_regime():
    with pytest.raises(ValueError):
        taxable_income(100000, "invalid", 0)


def test_taxable_income_negative():
    assert taxable_income(10000, "new", 0) == 0


# TAX DUE TESTS

def test_negative_taxable_income():
    with pytest.raises(ValueError):
        tax_due(-1000, 30)


def test_below_exemption():
    assert tax_due(200000, 30) == 0


def test_age_below_60():
    assert tax_due(400000, 30) == 7500


def test_age_between_60_and_79():
    assert tax_due(400000, 65) == 5000


def test_age_80_and_above():
    assert tax_due(600000, 80) == 5000


def test_higher_tax_slab():
    assert tax_due(800000, 30) == 72500


# REFUND STATUS TESTS

def test_refund_on_time():
    assert refund_status(50000, 30000, True) == "refund"


def test_refund_delayed():
    assert refund_status(50000, 30000, False) == "refund delayed"


def test_pay_balance_on_time():
    assert refund_status(30000, 50000, True) == "pay balance"


def test_pay_balance_late():
    assert refund_status(30000, 50000, False) == "pay balance with penalty"


def test_settled():
    assert refund_status(50000, 50000, True) == "settled"
