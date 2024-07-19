import re
import numpy as np
import matplotlib.pyplot as plt


class FunctionEvaluator:
    @staticmethod
    def evaluate_function(func, x):
        """Evaluates the function for the given x values."""
        try:
            # Replace the caret symbol (^) with the double asterisk (**) for power
            func = func.replace('^', '**')
            func = func.replace('X', 'x')

            # Replace math functions with numpy equivalents
            func = re.sub(r'\blog10\b', 'np.log10', func)
            func = re.sub(r'\bsqrt\b', 'np.sqrt', func)

            # Evaluate the function
            return eval(func)
        except Exception as e:
            raise ValueError(f"Error evaluating function: {e}")

    @staticmethod
    def plot_function(func, min_x, max_x):
        """Plots the user-entered function within the specified x range."""
        min_x = float(min_x)
        max_x = float(max_x)

        if min_x >= max_x:
            raise ValueError("Min x should be less than Max x.")

        x = np.linspace(min_x, max_x, 1000)
        y = FunctionEvaluator.evaluate_function(func, x)
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
