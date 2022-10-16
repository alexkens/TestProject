"""
This module shows some examples of Python Docstrings

Classes: Employee
Functions: multiply(a, b)
"""

def multiply(a, b):
    """Returns the multiplied sum of the args a and b."""
    return a*b


if __name__ == '__main__':
    sales = {'apple': 2, 'orange': 3, 'grapes': 4}

    print(type(sales))
    print(type(sales.items()))