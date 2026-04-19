from pydantic import BaseModel, Field


class VisualizationReport(BaseModel):
    csv_path: str = Field(..., description="Path to the input CSV file")
    chart_type: str = Field(..., description="Selected chart type")
    x_column: str = Field(..., description="Column used for x-axis")
    y_column: str = Field(..., description="Column used for y-axis")
    output_path: str = Field(..., description="Path to the saved chart image")
    explanation: str = Field(..., description="Short reason for choosing this chart")