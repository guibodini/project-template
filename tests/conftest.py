import pytest


@pytest.fixture
def sample_data() -> dict[str, int]:
    return {"a": 1, "b": 2}
