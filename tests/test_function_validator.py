import pytest
from function_validator import FunctionValidator


@pytest.mark.parametrize("func, expected", [
    ("X+1", True),
    ("X^2+5.5", True),
    ("(X+1)*2", True),
    ("(X+1)^2.5", True),
    ("(X+1)^2+5*3", True),
    ("(X+1)^2+5*3/2-log10(X)", True),
    ("(X+1)^2+5*3/2-log10(X)+sqrt(X)+X-1/2*3^2+X", True),
    ("(X+1)^2+5*3/2-log10(X)+sqrt(X)+X-1/2*3^2+X^2", True),
    ("log10(X)", True),
    ("X+Y", False),
    ("print('hi')", False),
    ("__import__('os').system('ls')", False),
    ("X=a", False),
])
def test_function_validation(func, expected):
    assert FunctionValidator.is_valid_function(func) == expected
