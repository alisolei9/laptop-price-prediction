from pathlib import Path

import pandas as pd


RAW_DATA_DIR = Path("data") / "raw"


def load_data(file_name: str) -> pd.DataFrame:
    """
    Load a dataset from the raw data directory.

    Parameters
    ----------
    file_name : str
        Dataset filename.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """
    file_path = RAW_DATA_DIR / file_name
    return pd.read_csv(file_path)
