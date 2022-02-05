import pytest
import numpy as np


@pytest.fixture(scope="function")
def random_array():
    return np.random.randint(1, 101, 500)

