from app.graph.workflow import run_visualization_workflow


def main() -> None:
    csv_path = input("Enter path to CSV file: ").strip()

    try:
        report = run_visualization_workflow(csv_path)

        print("\nVisualization Report")
        print("--------------------")
        print(f"CSV path: {report['csv_path']}")
        print(f"Chart type: {report['chart_type']}")
        print(f"X column: {report['x_column']}")
        print(f"Y column: {report['y_column']}")
        print(f"Output path: {report['output_path']}")
        print(f"Explanation: {report['explanation']}")

    except Exception as exc:
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()