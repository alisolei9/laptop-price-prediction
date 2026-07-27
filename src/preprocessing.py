import pandas as pd

COLUMN_MAPPING = {
    "Company": "company",
    "Product": "product",
    "TypeName": "type_name",
    "Inches": "inches",
    "ScreenResolution": "screen_resolution",
    "CPU_Company": "cpu_company",
    "CPU_Type": "cpu_type",
    "CPU_Frequency (GHz)": "cpu_frequency",
    "RAM (GB)": "ram",
    "Memory": "memory",
    "GPU_Company": "gpu_company",
    "GPU_Type": "gpu_type",
    "OpSys": "operating_system",
    "Weight (kg)": "weight",
    "Price (Euro)": "price",
}


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw dataset.
    """

    df = df.copy()

    df = df.rename(columns=COLUMN_MAPPING)

    return df
