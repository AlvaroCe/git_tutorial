"""
Functions
"""

import numpy as np


def sum_example(argument_1, argument_2):
    """
    Performs the sum of the two arguments passed.
        :param float argument_1:
        :param float argument_2:
        :return: The sum of both arguments
    """
    _sum = argument_1 + argument_2
    _sum = np.round(_sum, decimals=2)
    return _sum


def substract_example(argument_1, argument_2):
    """
    Performs the substraction of the two arguments passed.
        :param float argument_1: argument one
        :param float argument_2: argument two
        :returns: The substration of both arguments
    """
    _substract = argument_1 - argument_2
    _substract = np.round(_substract, decimals=2)
    return _substract

def division_example(argument_1, argument_2):
    """
    Performs the division of two elements.
        :param float argument_1: argument one
        :param float argument_2: argument two
        :returns: The division
    """
    division = argument_1 / (1.0 * argument_2)
    division = np.round(division, decimals=2)
    return division
