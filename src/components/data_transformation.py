import pandas as pd
import os

class Datatranformation:
    def __init__(self):
        self.rawdatapath=os.path.join("data","raw","rawdata.csv")
        self.encodeddatapath=os.path.join("data","transformed","transformeddata.csv")
    def transformdata(self):
        foldername=os.path.join("data","transformed")
        os.makedirs(foldername,exist_ok=True)
        data=pd.read_csv(self.rawdatapath)
        
        
        
        
        
        data.to_csv(self.encodeddatapath,index=False)
    