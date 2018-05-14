#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Martin
#
# Created:     10/05/2018
# Copyright:   (c) Martin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import logging
import math


def loggingTest():
    # Logging allows you to write status messages to a file
    # Each log message has a level. The five built-in levels are Debug, Info, Warning, Error, Critical

    import logging
    dir(logging)

    # Create and configure logger
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="C:\\Programy\\PythonProjects\\lumberjack.log", level = logging.DEBUG, format = LOG_FORMAT, filemode="w")
    logger = logging.getLogger()

    # Test the logger
    logger.info("Our first message.")

    logger.debug("This is a harmless debug message")
    logger.info("Just some useful info.")
    logger.warning("I'm sorry, but I can't do that, Dave.")
    logger.error("Did you just try to divide by zero?")
    logger.critical("The entire internet is down!!")

    print(logger.level)

    # Level     Numeric Value
    # NOTSET    0
    # DEBUG     10
    # INFO      20
    # WARNING   30
    # ERROR     40
    # CRITICAL  50


def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""

    # Set up logger
    # Create and configure logger
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="C:\\Programy\\PythonProjects\\lumberjack.log", level = logging.DEBUG, format = LOG_FORMAT, filemode="w")
    logger = logging.getLogger()

    # start logging
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c;

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1= (-b + math.sqrt(disc))/ (2*a)
    root2= (-b - math.sqrt(disc))/ (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return(root1, root2)


def main():
    #loggingTest()
    roots = quadratic_formula(1, 0, -4)
    print(roots)
    roots = quadratic_formula(1, 0, 1)
    print(roots)
    pass

if __name__ == '__main__':
    main()
