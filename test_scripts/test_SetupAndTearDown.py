import pytest
import os

def test_setup(temp_file):
    with open(temp_file,"r") as f:
        content = f.read()
        print(content)

    assert content == "Hello World!!" , "The content matches"

    assert os.path.exists(temp_file) , "The file does exist" "The file doesn't exist"