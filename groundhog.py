#!/usr/bin/python3

import sys

class Groundhog:
    """
    Class used to compute various statistics on a list of temperatures.
    """

    def __init__(self, period = 0):
        """
        Constructor of the class.
        """
        self.temperatures = []
        self.period = period

    class Error(Exception):
        """
        Base class for exceptions in this module.
        """

        def __init__(self, message):
            self.message = message

        def __str__(self):
            return self.message

    def getUserInput(self):
        """
        Get the user input.
        """
        temperature = input()
        if temperature == "STOP":
            return False
        try:
            self.temperatures.append(float(temperature))
            return True
        except ValueError:
            raise self.Error("Invalid input: please enter a number or STOP.")

    def computeAverage(self):
        """
        Computes the temperature increase average observed on the last period.
        """
        return 0

def handleArguments():
    """
    Handle the program arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: ./groundhog period")
        sys.exit(84)
    try:
        period = int(sys.argv[1])
    except ValueError:
        print("Invalid input: please enter a valid number.")
        sys.exit(84)
    if period <= 0:
        print("Invalid input: please enter a positive number.")
        sys.exit(84)
    return period
        return 0

def main():
    return 0

if __name__ == '__main__':
    main()
