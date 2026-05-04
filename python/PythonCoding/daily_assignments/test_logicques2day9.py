import pytest
@pytest.fixture
def sample_dict():
    return {"name": "Alice", "role": "Dev"}
def test_dict_keys(sample_dict):
    assert "role" in sample_dict
    assert sample_dict["name"] == "Alice"