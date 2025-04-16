"""
This is a boilerplate pipeline 'data_prosessing'
generated using Kedro 0.19.12
"""

import pandas as pd


def _is_true(x: pd.Series) -> pd.Series:
    return x == "t"


def _parse_money(x: pd.Series) -> pd.Series:
    return x.astype(str).str.replace("$", "").str.replace(",", "").astype(float)


def _parse_percentage(x: pd.Series) -> pd.Series:
    x = x.astype(str).str.replace("%", "")
    x = x.astype(float) / 100
    return x


def preprocess_companies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the companies dataframe.
    """
    df["iata_approved"] = _is_true(df["iata_approved"])
    df["company_rating"] = _parse_percentage(df["company_rating"])
    return df


def preprocess_shuttles(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the shuttles dataframe.
    """
    df["price"] = _parse_money(df["price"])
    df["d_check_complete"] = _is_true(df["d_check_complete"])
    df["moon_clearance_complete"] = _is_true(df["moon_clearance_complete"])

    return df


def create_model_input_table(
    shuttles: pd.DataFrame, companies: pd.DataFrame, reviews: pd.DataFrame
) -> pd.DataFrame:
    """
    Create the model input table by merging shuttles, companies and reviews dataframes.
    """
    # Merge shuttles and reviews dataframes
    reated_shuttles = shuttles.merge(reviews, left_on="id", right_on="shuttle_id")

    #  Merge shuttles and companies dataframes
    model_input_table = reated_shuttles.merge(
        companies, left_on="company_id", right_on="id"
    )

    return model_input_table.dropna()
