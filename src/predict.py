from pathlib import Path

import joblib
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "gradient_boosting_model.pkl"


def load_model():
    """
    Load trained Gradient Boosting model.
    """
    return joblib.load(MODEL_PATH)


def predict_price(features: pd.DataFrame):
    """
    Predict laptop prices.
    """
    model = load_model()

    prediction = model.predict(features)

    return prediction
