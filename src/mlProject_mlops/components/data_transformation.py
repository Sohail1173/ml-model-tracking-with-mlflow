import os
import urllib.request as request
import zipfile
from src.mlProject_mlops.utils.common import get_size
from src.mlProject_mlops.entity.config_entity import DataTransformationConfig
from src.mlProject_mlops.logging import logger
from pathlib import Path
from sklearn.model_selection import train_test_split
import pandas as pd



class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config=config
    


    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        train,test=train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

