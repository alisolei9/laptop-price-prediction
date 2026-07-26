from pathlib import Path

import pandas as pd


def load_data(filename: str) -> pd.DataFrame:
    """
    Load dataset from data/raw directory.
    """

    data_path = Path("data") / "raw" / filename

    return pd.read_csv(data_path)