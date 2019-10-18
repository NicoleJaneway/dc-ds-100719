import pytest
import pandas as pd 
from numpy import pi as truepi

@pytest.mark.question1
def test_if_list(conftest_list):
#   assert that the variable(arguement) is infact a list object.
    assert isinstance(conftest_list, list), "friends is not of type list"

@pytest.mark.question1
def test_length(conftest_list):
#   assert that the dictionary is 3 elements long.
    assert len(conftest_list) == 3, "This doesn't have 3 keys"

@pytest.mark.question2
def test_function(conftest_function, conftest_list):
#   assert that function exists.
    assert conftest_function, "You don't have a function called capitalize"
    
#   assert that the last name is uppercase.
    assert ~conftest_function(conftest_list)[0].islower()
    
@pytest.mark.question3
def test_dataframe(conftest_dataframe):
#   assert that animal_outcomes is a dataframe.
    assert isinstance(conftest_dataframe, pd.core.frame.DataFrame), "animal_outcomes is not a dataframe"
    
@pytest.mark.question3
def test_df_size(conftest_dataframe):
#   assert that the dataframe is of a certain size.
    assert conftest_dataframe.size == 1314336, "this dataframe is of the wrong size"
    
@pytest.mark.question3
def test_df_columns(conftest_dataframe):
#   assert that the dataframe is a certain number of columns.     
    assert len(conftest_dataframe.columns) == 12, "this dataframe doesn't have the right number of columns"
    
@pytest.mark.question4
def test_pi(conftest_pi):
    assert conftest_pi == truepi