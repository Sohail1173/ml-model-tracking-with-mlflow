from src.mlProject_mlops.config.configuration import ConfigurationManager
from src.mlProject_mlops.components.data_validation import DataValidation

STAGE_NAME="Data Validation stage"

class DataVlidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.gat_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()