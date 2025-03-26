import pandas as pd
import os 

class DataIngestion:
    def __init__(self):
        self.inputpath=os.path.join(r"D:\dataanalysis","students_performance","data","StudentsPerformance.csv")
        
        self.outputpath=os.path.join(r"D:\dataanalysis","students_performance","data","raw","rawdata.csv")
    def iniate_dataingestion(self):
        foldername=os.path.join(r"D:\dataanalysis","students_performance","data","raw")
        os.makedirs(foldername,exist_ok=True)
        data=pd.read_csv(self.inputpath)
        data.to_csv(self.outputpath,index=False)
        
        
        
        
        