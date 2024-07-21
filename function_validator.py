import re


class FunctionValidator:
    """Validates the user-entered function."""
    reg = r'(\d+\.?\d*|[+\-*/^()Xx]|log10|sqrt)'

    @staticmethod
    def is_valid_function(func):
        """Checks if the function is valid by tokenizing and checking each token."""
        tokens = FunctionValidator.tokenize(func)
        if ''.join(tokens) != func:
            return False
        for token in tokens:
            if not re.fullmatch(FunctionValidator.reg, token):
                return False
        return True

    @staticmethod
    def tokenize(expression):
        """Tokenizes the expression."""
        return re.findall(FunctionValidator.reg, expression)
