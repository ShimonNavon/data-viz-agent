from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def generate_chart(
    df: pd.DataFrame,
    chart_type: str,
    x_column: str,
    y_column: str,
    output_dir: str = "outputs",
) -> str:
    """
    Generate a chart and save it as a PNG file.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_path = Path(output_dir) / f"{chart_type}_{x_column}_{y_column}.png"

    plt.figure(figsize=(8, 5))

    if chart_type == "scatter":
        plt.scatter(df[x_column], df[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{y_column} vs {x_column}")

    elif chart_type == "bar":
        grouped = df.groupby(x_column)[y_column].sum()
        grouped.plot(kind="bar")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f"{y_column} by {x_column}")

    elif chart_type == "histogram":
        plt.hist(df[x_column], bins=20)
        plt.xlabel(x_column)
        plt.ylabel("Frequency")
        plt.title(f"Distribution of {x_column}")

    else:
        raise ValueError(f"Unsupported chart type: {chart_type}")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    return str(output_path)