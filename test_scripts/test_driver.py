import pytest

## function to load driver:
def load_driver(browser_name):
    driver= browser_name
    print(f"Driver name is {driver}")
    return driver


def test_driver():
    assert load_driver("Chrom") in ["Chrome","Firefox","Edge"], "Yes they are in List"


