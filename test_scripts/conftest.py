import os

import pytest


@pytest.fixture(params=[(6, 7, 13), (9, 9, 18)])
def add_parameters(request):
    return request.param


# specify browser
@pytest.fixture(params=["Chrome", "Firefox", "Edge"])
def browser_name(request):
    return request.param


# Setup and Teardown


@pytest.fixture(scope="function")
def temp_file(tmpdir_factory):
    file = "Text File"
    with open(file, "w") as f:
        f.write("Hello World!!")

    yield file

    os.remove(file)
    print("Test file has been cleaned")
