import re
from function_validator import FunctionValidator
import numpy as np


class FunctionEvaluator:
    """Evaluates the user-entered function for the given x values."""
    @staticmethod
    def evaluate_function(func, x):
        """Evaluates the function for the given x values."""
        # Replace the caret symbol (^) with the double asterisk (**) for power
        func = func.replace('X', 'x')
        # Remove spaces
        func = func.replace(' ', '')

        # Check if the function is valid (not malicious or having built-in functions)
        if not FunctionValidator.is_valid_function(func):
            raise ValueError("Error: Function contains invalid characters or built-in functions.")

        if re.search(r'/0\b', func):
            raise ZeroDivisionError("Error: Function contains a direct divide-by-zero operation.")

        if func == '':
            raise ValueError("Error: Function is empty.")

        # replace power operator with python equivalent
        func = func.replace('^', '**')
        # Replace math functions with numpy equivalents
        func = re.sub(r'\blog10\b', 'np.log10', func)
        func = re.sub(r'\bsqrt\b', 'np.sqrt', func)

        try:
            # Evaluate the function
            return eval(func)
        except Exception:
            raise ValueError(f"Error: Function contains an invalid expression.")
