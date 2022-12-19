# set up 
import pandas as pd 
import os 
from os.path import join as joinpath 
from dotenv import load_dotenv 

# load environment variables 
load_dotenv(verbose = True) 

# export model data as 'Model_data.csv' to ./processed/ 
def put_model_data_pro(df) -> None: 
    df.to_csv(joinpath(os.getenv('DATAPATH_PRO'), 'Model_Data.csv'), index = 0) 