"""
Basic script
"""

import maths

A = 5
B = 3

SUMA = maths.sum_example(A, B)
SUBSTRACTION = maths.substract_example(A, B)
print('The sum of {} and {} results: {} while the SUBSTRACTION results: {}'
      .format(A, B, SUMA, SUBSTRACTION))
