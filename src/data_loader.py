from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

DATA_FILE = "laptop_price - dataset.csv"


def load_data() -> pd.DataFrame:
    """
    Load raw dataset.
    """

    file_path = RAW_DATA_DIR / DATA_FILE

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    return pd.read_csv(file_path)
