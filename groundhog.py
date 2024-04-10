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

    def computeEvolution(self):
        """
        Computes the relative temperature evolution between the last given temperature and the temperature observed n-days ago.
        """
        return 0

    def computeDeviation(self):
        """
        Computes the standard deviation of the temperatures observed during the last period.
        """
        return 0

    def displayTrend(self):
        """
        Displays as soon as it detects a switch in global tendency or nothing if not.
        """
        return 0

def main():
    return 0

if __name__ == '__main__':
    main()
