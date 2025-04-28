import pytest

def find_letter(word,letter):
    for var in word:
        if var == letter:
            return True
    return False


@pytest.mark.xfail
def test_find_letter():
    assert find_letter("hello",'z')== True, "Function is correct" "Function is not correct"

