import pytest
from function_plotter import FunctionPlotter


def test_plot_function_valid_range():
    fig = FunctionPlotter.plot_function("X^2", -10, 10)
    assert fig is not None


def test_plot_function_invalid_range():
    with pytest.raises(ValueError):
        FunctionPlotter.plot_function("X^2", 10, -10)


def test_empty_plot():
    fig = FunctionPlotter.empty_plot(-10, 10)
    assert fig is not None
