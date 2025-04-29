import pytest

def find_letter(word,letter):
    for var in word:
        if var == letter:
            return True
    return False

@pytest.fixture(scope='module')
def fixture_demo():
    print(" I will run before the test cases which have this function called")
    yield
    print(" I will run after the test cases which have this function called")




def test_find_letter(fixture_demo):
    assert find_letter("hello",'o')== True, "Function is correct" "Function is not correct"





