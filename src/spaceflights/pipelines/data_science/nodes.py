"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.19.12
"""
import logging
import typing as t

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def split_data(df: pd.DataFrame, parameters:t.Dict) -> t.Tuple:
    X= df[parameters["fatures"]]
    Y= df["price"]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=parameters['test_size'])
    return X_train, X_test, Y_train, Y_test



def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> LinearRegression:
    """Trains the linear regression model.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    return regressor


def evaluate_model(
    regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series
):
    """Calculates and logs the coefficient of determination.

    Args:
        regressor: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    y_pred = regressor.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f on test data.", score)