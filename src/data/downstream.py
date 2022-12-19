# set up 
import pandas as pd 
import os 
from os.path import join as joinpath 
from dotenv import load_dotenv 

# load environment variables 
load_dotenv(verbose = True) 

# import cpi data from ./raw/ 
def get_cpi_raw() -> pd.DataFrame: 
    res = pd.read_csv(joinpath(os.getenv('DATAPATH_RAW'), 'CPI.csv'), header = 0) 

    return res 

# import national bond data from ./raw/ 
def get_bond_raw() -> pd.DataFrame: 
    res = pd.read_csv(joinpath(os.getenv('DATAPATH_RAW'), 'National_Bond.csv'), header = 0) 

    return res 

# import future data from ./raw/ 
def get_future_raw() -> pd.DataFrame: 
    res = pd.read_csv(joinpath(os.getenv('DATAPATH_RAW'), 'Future.csv'), header = 0) 

    return res 

# import model data from ./processed/ 
def get_model_data_pro() -> pd.DataFrame: 
    res = pd.read_csv(joinpath(os.getenv('DATAPATH_PRO'), 'Model_Data.csv'), header = 0) 

    return res 