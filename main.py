
import numpy as np
import matplotlib.pyplot as plt
import re
from sympy import sympify, symbols


def evaluate_function(func, x):
    """Evaluates the function for the given x values."""
    try:
        # Replace the caret symbol (^) with the double asterisk (**) for power
        func = func.replace('^', '**')

        # Replace math functions with numpy equivalents
        func = re.sub(r'\blog10\b', 'np.log10', func)
        func = re.sub(r'\bsqrt\b', 'np.sqrt', func)

        # Use eval to evaluate the function
        # my_function = sympify(func)
        # xx = symbols('x')
        # y = my_function.subs(xx, x)
        y = eval(func)
        return y
    except Exception as e:
        raise ValueError(f"Error evaluating function: {e}")


def plot_function(func, min_x, max_x):
    """Plots the user-entered function within the specified x range."""
    try:
        min_x = float(min_x)
        max_x = float(max_x)

        if min_x >= max_x:
            raise ValueError("Min x should be less than Max x.")

        x = np.linspace(min_x, max_x, 1000)
        y = evaluate_function(func, x)

        plt.figure()
        plt.plot(x, y, label=func)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function Plotter')
        plt.legend()
        plt.grid(True)
        plt.show()
    except ValueError as e:
        print(e)


def main():
    func = input("Enter function of x (e.g., 5*x**3 + 2*x): ")
    min_x = input("Enter min value of x: ")
    max_x = input("Enter max value of x: ")

    plot_function(func, min_x, max_x)


if __name__ == "__main__":
    main()
