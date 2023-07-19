import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging

from src.component.data_transformation import DataTransformation
from src.component.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion...")
        try:
            logging.info("Reading the dataset into dataframe...")
            df = pd.read_csv("./src/notebook/data/stud.csv")

            logging.info("Creating training directory...")
            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)

            logging.info("Writing raw data...")
            df.to_csv(self.ingestion_config.raw_data_path,
                      index=False, header=True)

            logging.info("Splitting train/test...")
            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,
                             index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)

            logging.info("Data has been ingested...")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    logging.info("Running data ingestion")
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transform = DataTransformation()
    train_arr, test_arr, _ = data_transform.initiate_data_transformation(
        train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
