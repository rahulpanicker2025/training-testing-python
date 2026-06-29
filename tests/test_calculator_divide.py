from __future__ import annotations

import sys

import pytest

from calculator import Calculator


def test__divide__given_two_valid_numbers__returns_their_quotient() -> None:
    # Arrange
    calc = Calculator()
    # Act
    result = calc.divide(3.0,3.0)
    # Assert
    assert result == pytest.approx(1.0,rel=1e-8)
    # pass

@pytest.mark.parametrize("x", [0.0, 1.5, -3.7, 1e15])
def test__divide__given_dividend_and_one__returns_dividend(x: float) -> None:
    # Arrange
    calc = Calculator()
    # Act
    result = calc.divide(x,1.0)
    # Assert
    assert result == pytest.approx(x,rel=1e-8)
    # pass

@pytest.mark.parametrize("a,b", [(1.0, 1.0), (1.5, 1.5), (1e10, 1e10), (2.0, 2.0)])
def test__divide__given_same_numbers__returns_one(a: float ,b: float) -> None:
    # Arrange
    calc = Calculator()
    # Act
    result = calc.divide(a,b)
    # Assert
    assert result == pytest.approx(1.0,rel=1e-8)
    # pass

@pytest.mark.parametrize("a,b,expected", [
    (1,   2.0, 0.5),  # int first operand promoted to float
    (1.0, 2,   0.5),  # int second operand promoted to float
])
def test__divide__given_int_operands__returns_float(a: int | float, b: int | float, expected: float) -> None:
    # Arrange
    calc = Calculator()
    # Act
    result = calc.divide(a,b)
    # Assert
    assert result == pytest.approx(expected, rel=1e-8)
    assert isinstance(result, float)
    # pass

@pytest.mark.parametrize("a,b", [
    ("1", 2.0),   # string as first operand
    (True, 2.0),  # bool as first operand
    (1.0, "2"),   # string as second operand
    (1.0, False), # bool as second operand
])
def test__divide__given_invalid_types__raises_type_error( a: object, b: object) -> None:
    # Arrange
    calc = Calculator()

    # ACT / ASSERT
    with pytest.raises(TypeError):
        calc.divide(a, b)  # type: ignore[arg-type]
    # pass

@pytest.mark.parametrize("a,b", [
    (float("inf"), 1.0),  # inf as first operand
    (1.0, float("nan")),  # nan as second operand
])
def test__divide__given_non_finite_operand__raises_value_error(a: float, b: float) -> None:
    # Arrange
    calc = Calculator()
    # ACT / ASSERT
    with pytest.raises(ValueError):
        calc.divide(a, b)

@pytest.mark.parametrize("x", [0.0, 1.5, -3.7, 1e15])
def test__divide__given_zero_divisor__raises_zero_division_error(x: float) -> None:
    # Arrange
    calc = Calculator()
    # ACT / ASSERT
    with pytest.raises(ZeroDivisionError):
        calc.divide(x, 0.0)
    # pass

def test__divide__given_inputs_that_overflow__raises_overflow_error() -> None:
    # Arrange
    calc = Calculator()
    # ACT / ASSERT
    with pytest.raises(OverflowError):
        calc.divide(sys.float_info.max, 0.9)
