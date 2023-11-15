from mlProject.constants import *
from mlProject.utils.common import read_yaml, create_directories
from mlProject.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    """
    Class responsible for managing the configuration of a machine learning project.

    Attributes:
        config_filepath (str): The filepath of the configuration YAML file.
        params_filepath (str): The filepath of the parameters YAML file.
        schema_filepath (str): The filepath of the schema YAML file.
        config (dict): The configuration data read from the configuration YAML file.
        params (dict): The parameter data read from the parameters YAML file.
        schema (dict): The schema data read from the schema YAML file.

    Methods:
        __init__(self, config_filepath, params_filepath, schema_filepath): Initializes the ConfigurationManager instance.
        get_data_ingestion_config(self) -> DataIngestionConfig: Returns the data ingestion configuration.

    """

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
    ):
        """
        Initializes the ConfigurationManager instance.

        Args:
            config_filepath (str, optional): The filepath of the configuration YAML file. Defaults to CONFIG_FILE_PATH.
            params_filepath (str, optional): The filepath of the parameters YAML file. Defaults to PARAMS_FILE_PATH.
            schema_filepath (str, optional): The filepath of the schema YAML file. Defaults to SCHEMA_FILE_PATH.
        """
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Returns the data ingestion configuration.

        Returns:
            DataIngestionConfig: The data ingestion configuration.
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config
