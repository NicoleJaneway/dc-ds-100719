import pytest
from example_index import friends, capitalize, animal_outcomes, pi

@pytest.fixture
def conftest_list():
    return friends

@pytest.fixture
def conftest_function():
    return capitalize

@pytest.fixture
def conftest_dataframe():
    return animal_outcomes

@pytest.fixture
def conftest_pi():
    return pi