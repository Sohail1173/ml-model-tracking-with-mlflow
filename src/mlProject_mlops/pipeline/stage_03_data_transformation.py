from src.mlProject_mlops.config.configuration import ConfigurationManager
from src.mlProject_mlops.components.data_transformation import DataTransformation
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                # status = f.read().split(" ")[-1]
                status = f.read().split(":")[-1]
            print(f"SSSSSSSSStatus:::::::{status}")

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)