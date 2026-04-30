import pytest

@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    print("Starting......")
    yield     # temporary hold
    # return  # permanent hold next part will never get executed example the next print
              # statement will not get print
    print("Ending........")

# def teardown():
#     pass

