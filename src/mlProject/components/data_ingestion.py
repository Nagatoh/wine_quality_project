import os
from urllib import request
import zipfile
from pathlib import Path
from mlProject import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initializes an instance of the DataIngestion class.

        Args:
            config (DataIngestionConfig): An object of the DataIngestionConfig class 
                                          that contains configuration parameters for data ingestion.

        Returns:
            None
        """
        self.config = config

    def download_file(self):
        """
        Downloads a file from a given URL and saves it locally.
    
        If the file already exists, logs the file size instead.
    
        Parameters:
            self (DataIngestion): The instance of the DataIngestion class.
        
        Returns:
            None
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with the following info: \n{headers}")
        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        """
        Extracts the zip file into the specified directory.

        Returns:
            None

        Raises:
            FileNotFoundError: If the zip file does not exist.
            zipfile.BadZipFile: If the zip file is corrupted or invalid.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
