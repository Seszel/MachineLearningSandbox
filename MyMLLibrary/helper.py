import pandas as pd
import numpy as np
import typing


def category_proportions(data: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """Counts proportion of samples in categories

    Args:
        data (pd.DataFrame): _description_
        column_name (str): _description_

    Returns:
        pd.DataFrame: _description_
    """

    return data[column_name].value_counts() / len(data)

def compare_proportions(data: pd.DataFrame, 
                        stratified_set: pd.DataFrame, 
                        random_set: pd.DataFrame,
                        column_name: str) -> pd.DataFrame:
    """Creates DataFrame which compares representativeness of various categories of column_name in dataset and counts

    Args:
        data (pd.DataFrame): _description_
        stratified_set (pd.DataFrame): _description_
        random_set (pd.DataFrame): _description_
        column_name (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    
    result = pd.DataFrame({
        "Overall %": category_proportions(data, column_name),
        "Stratified %": category_proportions(stratified_set, column_name),
        "Random %": category_proportions(random_set, column_name),
    }).sort_index()


    result.index.name = column_name
    result["Strat. Error %"] = (result["Stratified %"] / result["Overall %"] - 1)
    result["Rand. Error %"] = (result["Random %"] / result["Overall %"] - 1)

    return result