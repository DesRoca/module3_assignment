import pytest
from typing import Union
from app.operations import Operations

Number = Union[int, float]

@pytest.mark.parametrize(
    "a, b, expected", 
    [
        (1, 1, 2), # Test addition of two positive numbers
        (1, -1, 0), # Test addition of a positive and a negative number
        (-1, -1, -2), # Test addition of two negative numbers
        (0, 0, 0), # Test addition of two zeros
        (1.5, 2.5, 4.0), # Test addition of two floats 
        (-1.5, -2.5, -4.0), # Test addition of two negative floats
        (1.5, -2.5, -1.0), # Test addition of a positive float and a negative float
    ],
    ids=[
        "add two positive numbers",
        "add positive and negative number",
        "add two negative numbers",
        "add two zeros",
        "add two floats",
        "add two negative floats",
        "add positive and negative floats"
    ]
)

def test_addition(a: Number, b: Number, expected: Number) -> None:
    """
    Test the addition method of the Operations class.
    This test checks various cases of addition, including positive numbers, negative numbers, and floats.
    """
    result = Operations.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 0), # Test subtraction of two positive numbers
        (1, -1, 2), # Test subtraction of a positive and a negative number
        (-1, -1, 0), # Test subtraction of two negative numbers
        (0, 0, 0), # Test subtraction of two zeros
        (1.5, 2.5, -1.0), # Test subtraction of two floats 
        (-1.5, -2.5, 1.0), # Test subtraction of two negative floats
        (1.5, -2.5, 4.0), # Test subtraction of a positive float and a negative float
    ],
    ids=[
        "subtract two positive numbers",
        "subtract positive and negative number",
        "subtract two negative numbers",
        "subtract two zeros",
        "subtract two floats",
        "subtract two negative floats",
        "subtract positive and negative floats"
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    """
    Test the subtraction method of the Operations class.
    This test checks various cases of subtraction, including positive numbers, negative numbers, and floats.
    """
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 1), # Test multiplication of two positive numbers
        (1, -1, -1), # Test multiplication of a positive and a negative number
        (-1, -1, 1), # Test multiplication of two negative numbers
        (0, 0, 0), # Test multiplication of two zeros
        (1.5, 2.5, 3.75), # Test multiplication of two floats 
        (-1.5, -2.5, 3.75), # Test multiplication of two negative floats
        (1.5, -2.5, -3.75), # Test multiplication of a positive float and a negative float
    ],
    ids=[
        "multiply two positive numbers",
        "multiply positive and negative number",
        "multiply two negative numbers",
        "multiply two zeros",
        "multiply two floats",
        "multiply two negative floats",
        "multiply positive and negative floats"
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    """
    Test the multiplication method of the Operations class.
    This test checks various cases of multiplication, including positive numbers, negative numbers, and floats.
    """
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 1), # Test division of two positive numbers
        (1, -1, -1), # Test division of a positive and a negative number
        (-1, -1, 1), # Test division of two negative numbers
        (0, 1, 0), # Test division of zero by a positive number
        (0, -1, 0), # Test division of zero by a negative number 
        (1.5, 2.5, 0.6), # Test division of two floats
        (-1.5, -2.5, 0.6), # Test division of two negative floats
        (1.5, -2.5, -0.6), # Test division of a positive float and a negative float
    ],
    ids=[
        "divide two positive numbers",
        "divide positive and negative number",
        "divide two negative numbers",
        "divide zero by positive number",
        "divide zero by negative number",
        "divide two floats",
        "divide two negative floats",
        "divide positive and negative floats"
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None:
    """
    Test the division method of the Operations class.
    This test checks various cases of division, including positive numbers, negative numbers, and floats.
    """
    result = Operations.division(a, b)
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0), # Test division by zero with a positive number
        (-1, 0), # Test division by zero with a negative number
        (0, 0), # Test division by zero with zero
    ],
    ids=[
        "divide positive number by zero",
        "divide negative number by zero",
        "divide zero by zero"
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        Operations.division(1, 0)

    assert "Division by zero is not allowed." in str(excinfo.value), \
    f"Expected ValueError with message 'Division by zero is not allowed.', but got {excinfo.value}"