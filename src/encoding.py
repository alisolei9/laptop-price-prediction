import pandas as pd


def encode_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical features for machine learning.
    """

    df = df.copy()

    # Drop high-cardinality feature
    df = df.drop(columns="product")

    categorical_columns = [
        "company",
        "type_name",
        "cpu_company",
        "gpu_company",
        "operating_system",
        "cpu_family",
        "gpu_family",
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_columns,
        dtype=int
    )

    return df
