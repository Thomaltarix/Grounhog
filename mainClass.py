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
        self.standardDeviation = []
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

    def calculateAverage(self):
        """
        Calculates the standard deviation of the last period and returns it.
        """

        average = 0
        if not self.isEnougValues(self.period):
            return -1
        for i in range(self.period):
            average += self.temperatures[-1 - i]
        return (average / self.period)



    def computeDeviation(self):
        deviation = 0
        if self.isEnougValues(self.period):
            average = self.calculateAverage()
            for i in range(self.period):
                deviation += (self.temperatures[-1 - i] - average) ** 2
            deviation = (deviation / self.period) ** 0.5
            self.standardDeviation.append(deviation)
            print(f"s={deviation:.2f}", end="")
        else:
            self.standardDeviation.append(-1)
            print("s=nan", end="")
        return 0

    def displayTrend(self):
        """
        Displays as soon as it detects a switch in global tendency or nothing if not.
        """
        if self.trendChanged:
            print("\t\ta switch occurs")
            self.tendencyNb += 1
            self.trendChanged = False
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
        nbweird = 0
        weirddifference = []
        weirdnb = []
        for i in range(len(self.standardDeviation)):
            if self.standardDeviation[i] != -1 and (self.temperatures[-1 - i] > self.temperatures[-1] + 2 * self.standardDeviation[i]):
                weirddifference.append(self.temperatures[i] - self.temperatures[-1 - i] - self.standardDeviation[i])
                weirdnb.append(i)
        top_weird_values = []
        top_index = []
        for i in range(5):
            if len(weirddifference) == 0:
                break
            maxweird = max(weirddifference)
            top_index.append(weirdnb[weirddifference.index(maxweird)])
            weirddifference.remove(maxweird)
            top_weird_values.append(maxweird)
        final_weird_values = []
        for i in range(len(top_weird_values)):
            final_weird_values.append(self.temperatures[-1 - top_index[i]])

        print(len(top_weird_values), " weirdest values are ", final_weird_values)
