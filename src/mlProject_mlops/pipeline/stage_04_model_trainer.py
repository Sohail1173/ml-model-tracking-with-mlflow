from src.mlProject_mlops.config.configuration import ConfigurationManager
from src.mlProject_mlops.components.model_trainer import ModelTrainer
from src.mlProject_mlops.logging import logger



STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()