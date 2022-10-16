"""
This module shows some examples of Python Docstrings

Classes: Employee
Functions: multiply(a, b)
"""

def multiply(a, b):
    """Returns the multiplied sum of the args a and b."""
    return a*b

class Person:
    """This is a conceptual class representation of a simple BLE device
       (GATT Server). It is essentially an extended combination of the
       :class:`bluepy.btle.Peripheral` and :class:`bluepy.btle.ScanEntry` classes

       :param name: a name to the instance of the :class:`Person` 
       :type name: class:`str`
       :param age: age of the instance of the :class:`Person`
       :type age: int
       """
    def __init__(self, name, age):
        """Constructor method"""
        self.name = name
        self.age = age

    def showAge(self):
        """Prints out the age of the instance

        :return: just the age
        :rtype: int
        """

        print(self.age)
        return self.age


if __name__ == '__main__':
    sales = {'apple': 2, 'orange': 3, 'grapes': 4}

    print(type(sales))
    print(type(sales.items()))