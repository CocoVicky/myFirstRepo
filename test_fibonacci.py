"""
Unit tests for Fibonacci application
"""

from app import fib


def test_suite_fibonacci():
    """
    Test 10 first Fibonacci suite numbers
    """
    ten_first_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    ten_first_function_result = [fib(x, 0, 1) for x in range(10)]
    assert ten_first_function_result == ten_first_result
