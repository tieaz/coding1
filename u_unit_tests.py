# Chapter U ⇒ Unit Tests

from typing import *


def threesum(nums: List[int]) -> List[int]:
  nums.sort()
  for i in range(len(nums) - 2):
    j = i + 1
    k = len(nums) - 1
    while j < k:
      target = nums[i] + nums[j] + nums[k]
      if target == 0:
        return [nums[i], nums[j], nums[k]]
      elif target < 0:
        j +=1
      else:
        k -= 1

  return None


import unittest

# class ThreesumTestCase(unittest.TestCase):
#   def testFalse(self):
#     self.assertTrue(False)

# unittest.main()
# >>> Console
# % python3 unity.py
# F
# ======================================================================
# FAIL: testFalse (__main__.ThreesumTestCase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "unity.py", line 28, in testFalse
#     self.assertTrue(False)
# AssertionError: False is not true

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=1)


class ThreesumTestCase(unittest.TestCase):
  def setUp(self):
    self.arr = [-3,2,-1,1,3,-6]

  def testTooFewElements(self):
    self.assertIsNone(threesum([]))
    self.assertIsNone(threesum([1]))
    self.assertIsNone(threesum([1,2]))

  def testNoSolution(self):
    self.assertIsNone(threesum([1,2,3]))
    self.assertIsNone(threesum([-3,-1,-2]))

  def testSolution(self):
    self.assertEqual([-3, 1, 2], threesum(self.arr))


def atoi(str):
  if not str: raise ValueError('no digits')
  m = len(str)

  # Consume leading whitespace.
  ix = 0
  while ix < m and str[ix] == ' ': ix += 1
  if ix == m: raise ValueError('no digits')

  # Detect sign.
  is_negative = str[ix] == '-'
  if str[ix] in ('-', '+'):
      ix += 1

  if ix == m: raise ValueError('no digits')

  # Consume digits.
  num = 0
  while ix < m and ('0' <= str[ix] <= '9'):
      num = 10 * num + (ord(str[ix]) - ord('0'))
      ix += 1

  if ix < m: raise ValueError('invalid characters')
  # Return number:
  return num * (-1 if is_negative else 1)


class AtoiTestCase(unittest.TestCase):
  def testInvalid(self):
    with self.assertRaises(ValueError):
      atoi('')
    with self.assertRaises(ValueError):
      atoi('     ')
    with self.assertRaises(ValueError):
      atoi('     -')
    with self.assertRaises(ValueError):
      atoi('     +')
    with self.assertRaises(ValueError):
      atoi('     -1234a345')
    with self.assertRaises(ValueError):
      atoi('     1234a345')

  def testValid(self):
    self.assertEqual(atoi('0'), 0)
    self.assertEqual(atoi('1'), 1)
    self.assertEqual(atoi('-0'), 0)
    self.assertEqual(atoi(' -0'), 0)
    self.assertEqual(atoi('123'), 123)
    self.assertEqual(atoi('   123'), 123)
    self.assertEqual(atoi('-123456'), -123456)
    self.assertEqual(atoi('123456'), 123456)

unittest.main()
