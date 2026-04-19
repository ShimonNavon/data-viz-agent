from typing import TypedDict

from langgraph.graph import END, StateGraph

from app.schemas.report import VisualizationReport
from app.services.chart_selector import choose_chart
from app.tools.chart_generator import generate_chart
from app.tools.data_loader import load_csv


class VizState(TypedDict, total=False):
    csv_path: str
    chart_type: str
    x_column: str
    y_column: str
    output_path: str
    explanation: str


def inspect_data(state: VizState) -> VizState:
    df = load_csv(state["csv_path"])
    decision = choose_chart(df)
    return {
        "csv_path": state["csv_path"],
        "chart_type": decision["chart_type"],
        "x_column": decision["x_column"],
        "y_column": decision["y_column"],
        "explanation": decision["explanation"],
    }


def create_chart(state: VizState) -> VizState:
    df = load_csv(state["csv_path"])
    output_path = generate_chart(
        df=df,
        chart_type=state["chart_type"],
        x_column=state["x_column"],
        y_column=state["y_column"],
    )
    return {
        **state,
        "output_path": output_path,
    }


def build_report(state: VizState) -> VizState:
    report = VisualizationReport(
        csv_path=state["csv_path"],
        chart_type=state["chart_type"],
        x_column=state["x_column"],
        y_column=state["y_column"],
        output_path=state["output_path"],
        explanation=state["explanation"],
    )
    return report.model_dump()


def create_workflow():
    graph = StateGraph(VizState)

    graph.add_node("inspect_data", inspect_data)
    graph.add_node("create_chart", create_chart)
    graph.add_node("build_report", build_report)

    graph.set_entry_point("inspect_data")
    graph.add_edge("inspect_data", "create_chart")
    graph.add_edge("create_chart", "build_report")
    graph.add_edge("build_report", END)

    return graph.compile()


app = create_workflow()


def run_visualization_workflow(csv_path: str) -> dict:
    return app.invoke({"csv_path": csv_path})