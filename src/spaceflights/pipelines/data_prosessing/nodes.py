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
    #df["d_check_completed"] = _is_true(df["d_check_completed"])
    df["moon_clearance_complete"] = _is_true(df["moon_clearance_complete"])

    return df
