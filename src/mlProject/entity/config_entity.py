from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Represents the configuration for data ingestion.

    Attributes:
        root_dir (Path): The root directory where the data will be stored.
        source_URL (str): The URL from where the data will be downloaded.
        local_data_file (Path): The local file path where the downloaded data will be stored.
        unzip_dir (Path): The directory where the downloaded data will be unzipped.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
