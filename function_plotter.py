import numpy as np
import matplotlib.pyplot as plt
from function_evaluator import FunctionEvaluator


class FunctionPlotter:
    """Plots the user-entered function within the specified x range."""
    @staticmethod
    def plot_function(func, min_x, max_x):
        """Plots the user-entered function within the specified x range."""
        min_x = float(min_x)
        max_x = float(max_x)

        if min_x >= max_x:
            raise ValueError("Min x should be less than Max x.")

        x = np.linspace(min_x, max_x, 1000)
        y = FunctionEvaluator.evaluate_function(func, x)
        if type(y) in [int, float]:
            y = np.full_like(x, y)
        fig = plt.figure()
        plt.plot(x, y)
        plt.title(f'f(x) = {func.replace("X", "x")}')
        plt.xlabel('x')
        plt.ylabel('f (x)')
        plt.grid(True)
        return fig

    @staticmethod
    def empty_plot():
        """Returns an empty plot."""
        fig = plt.figure()
        plt.xlabel('x')
        plt.ylabel('f (x)')
        plt.grid(True)
        return fig
