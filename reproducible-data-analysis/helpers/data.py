import os
import pandas as pd
from urllib.request import urlretrieve

# Define helper functions

# Fremont data url
FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

# Download the Fremont data if it doesn't exist already
def get_fremont_data(file_name='Fremont.csv', url=FREMONT_URL, force_download=False):
    """
    Download and cache Fremont data

    Parameters
    ----------
    file_name : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data

    Returns
    -------
    data : pandas.DataFrame
        The Fremont bridge data
    """
    if force_download or not os.path.exists(file_name):
        urlretrieve(URL, file_name)

    fremont_df = pd.read_csv('Fremont.csv', index_col='Date')
    fremont_df.columns = ['Total', 'East', 'West']
    try:
        fremont_df.index = pd.to_datetime(fremont_df.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        fremont_df.index = pd.to_datetime(fremont_df.index)

    return fremont_df
