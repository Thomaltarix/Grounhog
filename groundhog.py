#!/usr/bin/python3

import sys
import mainClass

def mainLoop(Groundhog):
    """
    Main loop of the program.
    """
    try:
        while Groundhog.catchUserInput():
            Groundhog.computeAverage()
            Groundhog.computeEvolution()
            Groundhog.computeDeviation()
            Groundhog.displayTrend()
    except Groundhog.Error as error:
        print(error)
        sys.exit(84)
    Groundhog.displayTendencyNb()
    Groundhog.displayWeirdValues()
    print(f"Les valeurs sont : {Groundhog.temperatures}")
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

def main():
    """
    Main function of the program.
    """
    period = handleArguments()
    Groundhog = mainClass.Groundhog(period)
    return mainLoop(Groundhog)

if __name__ == '__main__':
    main()
