import pandas as pd


def get_feature_importance(model, feature_names):
    """
    Return sorted feature importance DataFrame.
    """

    importance = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": model.feature_importances_,
        }
    )

    importance = importance.sort_values(
        by="Importance",
        ascending=False,
    ).reset_index(drop=True)

    return importance
