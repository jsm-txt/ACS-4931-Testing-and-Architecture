import unittest
from unittest import mock
import py
import pytest
import math
# from ..calculate_grades import calculate_stat

import sys
sys.path.append("..") 

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    if grade_list == []:
        raise ValueError()
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

print(calculate_stat([1,2,3]))
def test_calculate_stat():
  assert calculate_stat([1,2,3]) ==(2.0, 0.816496580927726)
  with pytest.raises(ValueError):
   calculate_stat([]) 
  with pytest.raises(TypeError):
    calculate_stat('sdsd')