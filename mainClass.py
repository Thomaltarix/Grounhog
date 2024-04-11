#!/usr/bin/python3

from enum import Enum

class Groundhog:
    """
    Class used to compute various statistics on a list of temperatures.
    """

    class SignedValue (Enum):
        """
        Enum used to determine if a value is positive, negative or null.
        """
        POSITIVE = 1
        NEGATIVE = -1
        NULL = 0

        def __not__(self):
            if self == self.POSITIVE:
                return self.NEGATIVE
            if self == self.NEGATIVE:
                return self.POSITIVE
            return self.NULL

    class Error(Exception):
        """
        Base class for exceptions in this module.
        """
        def __init__(self, message):
            self.message = message

    def __init__(self, period = 0):
        """
        Constructor of the class.
        """
        self.temperatures = []
        self.period = period
        self.tendencyNb = 0
        self.lastEvolution = 0
        self.weirdValues = []
        self.trendChanged = False

    def catchUserInput(self):
        """
        Get the user input.
        """
        temperature = input()
        if temperature == "STOP":
            return False
        try:
            self.temperatures.append(float(temperature))
        except ValueError:
            raise self.Error("Invalid input: please enter a number or STOP.")
        return True

    def isEnougValues(self, period = 0):
        """
        Returns True if there are enough values to compute the statistics.
        """
        return len(self.temperatures) >= period

    def computeAverage(self):
        """
        Computes the temperature increase average observed on the last period.
        """
        if self.isEnougValues(self.period + 1):
            result = 0
            for i in range(self.period):
                if self.temperatures[-1 - i] > self.temperatures[-2 - i]:
                    result += self.temperatures[-1 - i] - self.temperatures[-2 - i]
            result /= self.period
            print(f"g={result:.2f}\t\t", end="")
        else:
            print("g=nan\t\t", end="")
        return 0

    def getSign(self, value):
        """
        Returns the sign of a value.
        """
        if value > 0:
            return self.SignedValue.POSITIVE
        if value < 0:
            return self.SignedValue.NEGATIVE
        return self.SignedValue.NULL

    def computeEvolution(self):
        """
        Computes the relative temperature evolution between the last given temperature and the temperature observed n-days ago.
        """
        result = 0
        if self.isEnougValues(self.period + 1):
            result = (self.temperatures[-1] - self.temperatures[-1 - self.period]) / self.temperatures[-1 - self.period] * 100
            print(f"r={result:.0f}%\t\t", end="")
        else:
            print("r=nan%\t\t", end="")
        if self.getSign(result) != self.getSign(self.lastEvolution):
            self.trendChanged = True
        if (self.getSign(result) == self.SignedValue.NULL or self.getSign(self.lastEvolution) == self.SignedValue.NULL):
            self.trendChanged = False
        self.lastEvolution = result
        return 0

    def computeDeviation(self):
        """
        Computes the standard deviation of the temperatures observed during the last period.
        """
        result = 0
        if self.isEnougValues(self.period):
            print(f"s={result:.2f}", end="")
        else:
            print("s=nan", end="")
        return 0

    def displayTrend(self):
        """
        Displays as soon as it detects a switch in global tendency or nothing if not.
        """
        trend = False
        if trend:
            print("\t\ta switch occurs")
            self.tendencyNb += 1
        else:
            print("")
        return 0

    def displayTendencyNb(self):
        """
        Displays the number of tendencies switches from the beginning.
        """
        print("Global tendency switched", self.tendencyNb, "times")

    def displayWeirdValues(self):
        """
        Displays the number of values that are considered as weird.
        """
        print ("Weird values:", self.weirdValues)
