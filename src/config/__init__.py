
import os
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    input_data_path:str=os.path.join("data","StudentsPerformance.csv")
    raw_data_path:str=os.path.join("data","raw","raw.csv")
    
@dataclass
class DataTransformationConfig:
    raw_data_path:str=os.path.join("data","raw","raw.csv")
    transformed_data_path:str=os.path.join("data","transformed","transformed_data.csv")