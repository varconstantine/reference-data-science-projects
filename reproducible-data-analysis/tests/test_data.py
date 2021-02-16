# Import the modules that are going to be tested
from helpers.data import get_fremont_data
import pandas as pd
import numpy as np

# Get the data
data = get_fremont_data()

# Test the data shape: columns and index
def test_fremont_data():
    assert all(data.columns == ['Total', 'East', 'West'])
    assert isinstance(data.index, pd.DatetimeIndex)
    assert len(np.unique(data.index.time) == 24)