import pandas as pd
import os 
from dataclasses import dataclass
from src.config import DataIngestionConfig



class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        
        
        
    def iniate_dataingestion(self):
       
        folder= os.path.dirname(self.ingestion_config.raw_data_path) 
        os.makedirs(folder,exist_ok=True)
        data=pd.read_csv(self.ingestion_config.input_data_path)
        data.to_csv(self.ingestion_config.raw_data_path,index=False)

        