import pytest
import os

@pytest.fixture
def temp_file():
    filename = "test.txt"

    with open(filename, "w") as f:
        f.write("Hello World")

    yield filename

    if os.path.exists(filename):
        os.remove(filename)

def test_file_content(temp_file):
    with open(temp_file, "r") as f:
        content = f.read()

    assert content == "Hello World"