import pandas as pd


def load_csv(csv_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(csv_path)