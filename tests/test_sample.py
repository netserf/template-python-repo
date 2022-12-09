"""Sample test module for package_name"""

from package_name import sample


def test_pass():
    """Sample test function"""
    assert True, "dummy sample test"


def test_sample_function():
    """Sample test function using package_name.sample.sample_function"""
    assert sample.sample_function(), "sample function should return True"
