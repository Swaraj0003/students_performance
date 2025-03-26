import pandas as pd
import os
from dataclasses import dataclass
from src.config import DataTransformationConfig

class DataTransform:
    def __init__(self):
        self.transform_config=DataTransformationConfig()
        
        
        
    def iniate_datatransform(self):
       
        folder= os.path.dirname(self.transform_config.transformed_data_path) 
        os.makedirs(folder,exist_ok=True)
        data=pd.read_csv(self.transform_config.raw_data_path)
        data.to_csv(self.transform_config.transformed_data_path,index=False)
        
