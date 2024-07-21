import pytest
from function_evaluator import FunctionEvaluator
import numpy as np


@pytest.mark.parametrize("func, x_value, expected", [
    ("X+1", np.array([1, 2, 3]), np.array([2, 3, 4])),
    ("X^2", np.array([1, 2, 3]), np.array([1, 4, 9])),
    ("(X+1)^2", np.array([1, 2, 3]), np.array([4, 9, 16])),
    ("(X+1)^2+5*3", np.array([1, 2, 3]), np.array([19, 24, 31])),
    ("2*X+10", np.array([1, 2, 3]), np.array([12, 14, 16])),
    ("X/0", np.array([1, 2, 3]), pytest.raises(ZeroDivisionError)),
    ("X+Y", np.array([1, 2, 3]), pytest.raises(ValueError)),
    ("print('hi')", np.array([1, 2, 3]), pytest.raises(ValueError)),
    ("__import__('os').system('ls')", np.array([1, 2, 3]), pytest.raises(ValueError)),
    ("X=a", np.array([1, 2, 3]), pytest.raises(ValueError)),
])
def test_evaluate_function(func, x_value, expected):
    if not isinstance(expected, np.ndarray):
        with expected:

            FunctionEvaluator.evaluate_function(func, x_value)
    else:
        assert np.allclose(FunctionEvaluator.evaluate_function(func, x_value), expected)


def test_large_input():
    min_x, max_x = 1, 10000
    func = "X^2+log10(X)+sqrt(X)"
    x = np.linspace(min_x, max_x, 1000)
    y = FunctionEvaluator.evaluate_function(func, x)
    real_y = x**2 + np.log10(x) + np.sqrt(x)
    assert np.allclose(y, real_y)

    min_x, max_x = -10000, 10000
    func = "X^4*19+X^3*5+X^2*3+X*2+1"
    x = np.linspace(min_x, max_x, 1000)
    y = FunctionEvaluator.evaluate_function(func, x)
    real_y = x**4*19 + x**3*5 + x**2*3 + x*2 + 1
    assert np.allclose(y, real_y)

