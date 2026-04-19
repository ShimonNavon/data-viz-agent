<div align="center">

# Data Visualization Agent

<p>
  A small <strong>LangGraph-based</strong> project that loads a CSV file,
  inspects the dataset, chooses an appropriate chart, generates a visualization,
  and returns a <strong>structured report</strong>.
</p>

<p>
  This project is designed as a practical MVP for learning
  <strong>manual tool calling</strong>, <strong>workflow orchestration</strong>,
  and <strong>structured outputs</strong>.
  
  

</p>



https://github.com/user-attachments/assets/2e4412a9-8b35-40d5-ac45-8e410db51f10




In short: your input is a CSV and you get a chart







  <img width="1517" height="598" alt="Screenshot 2026-04-19 at 5 21 10 PM" src="https://github.com/user-attachments/assets/ae11b758-021a-437b-a532-01b73dfb40c5" />





<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-green">
  <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-Workflow-blue">
  <img alt="Pandas" src="https://img.shields.io/badge/Pandas-Data%20Handling-purple">
  <img alt="Matplotlib" src="https://img.shields.io/badge/Matplotlib-Charts-orange">
  <img alt="Output" src="https://img.shields.io/badge/Output-Structured-red">
</p>

</div>

---

## Project Goal

The goal of this project is to build a small data visualization agent that can:

<ul>
  <li>load a CSV file,</li>
  <li>inspect the dataset,</li>
  <li>select an appropriate chart type,</li>
  <li>generate the chart,</li>
  <li>and return a structured summary of what it did.</li>
</ul>

<p><strong>One-sentence version:</strong> We are building a small agent that turns tabular data into an automatically selected visualization through a controlled LangGraph workflow.</p>

---

## Main Learning Goals

<ul>
  <li><strong>Manual tool calling</strong> — the workflow explicitly calls data-loading and chart-generation tools.</li>
  <li><strong>Structured outputs</strong> — the final result follows a fixed schema.</li>
  <li><strong>Basic LangGraph workflow design</strong> — the project uses graph nodes and state transitions.</li>
  <li><strong>Rule-based chart selection</strong> — the system decides which chart to use based on column types.</li>
</ul>

---

## How It Works

<pre>
User provides CSV path
        ↓
LangGraph StateGraph
        ↓
inspect_data node
        ↓
load_csv tool
        ↓
choose_chart service
        ↓
create_chart node
        ↓
generate_chart tool
        ↓
build_report node
        ↓
Structured visualization report
</pre>

---

## Project Structure

<pre>
data-viz-agent/
├── app/
│   ├── graph/
│   │   └── workflow.py
│   ├── tools/
│   │   ├── data_loader.py
│   │   └── chart_generator.py
│   ├── schemas/
│   │   └── report.py
│   ├── services/
│   │   └── chart_selector.py
│   └── main.py
├── outputs/
└── tests/
</pre>

---

## Core Components

<table>
  <tr>
    <th align="left">Component</th>
    <th align="left">Purpose</th>
  </tr>
  <tr>
    <td><code>load_csv(csv_path)</code></td>
    <td>Loads a CSV file into a pandas DataFrame.</td>
  </tr>
  <tr>
    <td><code>choose_chart(df)</code></td>
    <td>Inspects the DataFrame and selects a chart type using simple rules.</td>
  </tr>
  <tr>
    <td><code>generate_chart(...)</code></td>
    <td>Creates and saves a visualization as a PNG file.</td>
  </tr>
  <tr>
    <td><code>VisualizationReport</code></td>
    <td>Defines the structured result returned by the workflow.</td>
  </tr>
  <tr>
    <td>LangGraph workflow</td>
    <td>Coordinates inspection, chart generation, and report-building steps.</td>
  </tr>
</table>

---

## Manual Tool Calling Explained

In this project, tool calling is <strong>manual</strong> because the workflow explicitly decides when to call tools such as:

<ul>
  <li><code>load_csv(csv_path)</code></li>
  <li><code>generate_chart(...)</code></li>
</ul>

The workflow directly invokes those functions in code. The model is not autonomously deciding whether or when to call them.

<pre><code>df = load_csv(state["csv_path"])
decision = choose_chart(df)
</code></pre>

This is the central learning pattern of the project.

---

## Structured Output Schema

The agent returns a fixed schema with fields such as:

<ul>
  <li><code>csv_path</code></li>
  <li><code>chart_type</code></li>
  <li><code>x_column</code></li>
  <li><code>y_column</code></li>
  <li><code>output_path</code></li>
  <li><code>explanation</code></li>
</ul>

This makes the output predictable, easy to validate, and easy to use in later systems.

---

## Chart Selection Logic

The current MVP uses simple rules:

<ul>
  <li><strong>2 or more numeric columns</strong> → scatter plot</li>
  <li><strong>1 numeric + 1 non-numeric column</strong> → bar chart</li>
  <li><strong>1 numeric column only</strong> → histogram</li>
</ul>

This keeps the system simple, transparent, and easy to improve later.

---

## Example Workflow Behavior

### Input CSV

<pre>
month,revenue
Jan,120
Feb,150
Mar,170
Apr,160
</pre>

### Result

<ul>
  <li>CSV is loaded</li>
  <li>Columns are inspected</li>
  <li>Agent selects a bar chart</li>
  <li>Chart is generated and saved</li>
  <li>Structured report is printed</li>
</ul>

---

## How to Run

### 1. Create and activate a virtual environment

<pre><code>python3 -m venv .venv
source .venv/bin/activate</code></pre>

### 2. Install dependencies

<pre><code>python -m pip install pandas matplotlib langgraph pydantic</code></pre>

### 3. Run the application

<pre><code>python -m app.main</code></pre>

The app will prompt you for a CSV path.

---

## Example Output

<pre>
Visualization Report
--------------------
CSV path: data/sample.csv
Chart type: bar
X column: month
Y column: revenue
Output path: outputs/bar_month_revenue.png
Explanation: Selected a bar chart because the dataset has one categorical column and one numeric column.
</pre>

---

## Why This Project Is Useful

<ul>
  <li>It is small enough to finish quickly.</li>
  <li>It demonstrates real workflow orchestration.</li>
  <li>It produces a visible artifact: a generated chart.</li>
  <li>It is a clean base for future upgrades like LLM chart selection, FastAPI, or a frontend UI.</li>
</ul>

---

## Future Improvements

<ul>
  <li>Add support for more chart types such as line charts and box plots.</li>
  <li>Allow user questions like “show me revenue by month.”</li>
  <li>Add LLM-based chart reasoning on top of the rule-based logic.</li>
  <li>Expose the workflow through FastAPI.</li>
  <li>Build a simple frontend for file upload and chart display.</li>
  <li>Add persistent storage for generated reports.</li>
</ul>

---

<div align="center">
  Built as a learning project for <strong>LangGraph</strong>, <strong>manual tool calling</strong>, and <strong>structured data visualization workflows</strong>.
</div>
