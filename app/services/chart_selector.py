import pandas as pd


def choose_chart(df: pd.DataFrame) -> dict:
    """
    Very simple rule-based chart selection.

    Rules:
    - 2+ numeric columns -> scatter
    - 1 numeric + 1 non-numeric -> bar
    - 1 numeric only -> histogram
    """

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    non_numeric_columns = [col for col in df.columns if col not in numeric_columns]

    if len(numeric_columns) >= 2:
        return {
            "chart_type": "scatter",
            "x_column": numeric_columns[0],
            "y_column": numeric_columns[1],
            "explanation": "Selected a scatter plot because the dataset has at least two numeric columns.",
        }

    if len(numeric_columns) >= 1 and len(non_numeric_columns) >= 1:
        return {
            "chart_type": "bar",
            "x_column": non_numeric_columns[0],
            "y_column": numeric_columns[0],
            "explanation": "Selected a bar chart because the dataset has one categorical column and one numeric column.",
        }

    if len(numeric_columns) == 1:
        return {
            "chart_type": "histogram",
            "x_column": numeric_columns[0],
            "y_column": numeric_columns[0],
            "explanation": "Selected a histogram because the dataset has one numeric column.",
        }

    raise ValueError("Could not determine a supported chart for this dataset.")