import streamlit as st

# ---------------------------
# Data Structure for 30 Days
# ---------------------------
# We’ll break it into 5 phases:
#   Phase 1 (Days 1-6): Basics
#   Phase 2 (Days 7-12): Visualization
#   Phase 3 (Days 13-18): Automation
#   Phase 4 (Days 19-24): Forecasting
#   Phase 5 (Days 25-30): Advanced
# Each day includes a short description + a mini project idea.

days_plan = {
    1: {
        "title": "Day 1: Getting Started with Python & Google Colab",
        "content": """
- **Overview**: Learn how to set up a Google Colab notebook and run basic Python code.
- **Mini Project**: Write a simple "Hello, FP&A World!" program, then play with basic arithmetic operations.
        """
    },
    2: {
        "title": "Day 2: Handling Your First Python Errors",
        "content": """
- **Overview**: Understand common error messages and how to ask ChatGPT (or other resources) for help.
- **Mini Project**: Purposefully generate errors (e.g., syntax errors) and practice debugging them.
        """
    },
    3: {
        "title": "Day 3: ChatGPT for Generating Python Code",
        "content": """
- **Overview**: Explore how to use ChatGPT to scaffold simple scripts for finance tasks.
- **Mini Project**: Ask ChatGPT to create a basic script that calculates a monthly budget or a savings plan.
        """
    },
    4: {
        "title": "Day 4: Using Python Libraries for Finance",
        "content": """
- **Overview**: Get familiar with libraries like `pandas`, `numpy`, and `yfinance`.
- **Mini Project**: Use `pandas` to read in a CSV file with sample financial data and do basic data inspection.
        """
    },
    5: {
        "title": "Day 5: Adding Data into Your Python Environment",
        "content": """
- **Overview**: Learn how to import data from various sources (local, Google Drive, CSV, Excel).
- **Mini Project**: Load a CSV of revenue and expenses, then calculate net income in Python.
        """
    },
    6: {
        "title": "Day 6: Python as a Pivot Table",
        "content": """
- **Overview**: Practice grouping and summarizing data with `pandas` groupby (similar to pivot tables).
- **Mini Project**: Create a pivot table-like summary of sales data grouped by product or region.
        """
    },
    7: {
        "title": "Day 7: Simple Bar Chart in Python",
        "content": """
- **Overview**: Learn the basics of data visualization with libraries like `matplotlib` or `seaborn`.
- **Mini Project**: Plot a bar chart comparing expenses across different months.
        """
    },
    8: {
        "title": "Day 8: Seaborn Library Essentials",
        "content": """
- **Overview**: Dive deeper into `seaborn` for more advanced visuals (e.g., count plot, box plot).
- **Mini Project**: Visualize a dataset's distribution using `seaborn`'s histogram or density plot.
        """
    },
    9: {
        "title": "Day 9: Box Plot for Statistical Analysis",
        "content": """
- **Overview**: Understand box plots, outliers, quartiles, and how to interpret them.
- **Mini Project**: Plot a box plot of monthly sales or budget data to see outliers.
        """
    },
    10: {
        "title": "Day 10: Correlation Analysis with Heatmap",
        "content": """
- **Overview**: Learn how to compute correlations and visualize them via heatmaps.
- **Mini Project**: Use a sample financial dataset to create a heatmap of correlations among variables.
        """
    },
    11: {
        "title": "Day 11: Customizing Any Data Visualization",
        "content": """
- **Overview**: Adjust labels, colors, legends, and style to build compelling dashboards.
- **Mini Project**: Take a bar chart or line chart and fully customize it (title, axis labels, color palette).
        """
    },
    12: {
        "title": "Day 12: Creating Your First Dashboard using Plotly",
        "content": """
- **Overview**: Use Plotly to build interactive charts and mini dashboards.
- **Mini Project**: Create an interactive dashboard to analyze revenue vs. expenses over time.
        """
    },
    13: {
        "title": "Day 13: Cleaning Up Data using Python",
        "content": """
- **Overview**: Handle missing values, remove duplicates, rename columns, and standardize data.
- **Mini Project**: Load messy financial data and clean it up using `pandas` (drop duplicates, fill missing).
        """
    },
    14: {
        "title": "Day 14: Automate Simple Finance Tasks",
        "content": """
- **Overview**: Write Python scripts that execute repetitive tasks (e.g., monthly data processing).
- **Mini Project**: Automate monthly data merging and produce a quick summary report.
        """
    },
    15: {
        "title": "Day 15: Merging Multiple Files",
        "content": """
- **Overview**: Practice combining data from various Excel/CSV files (like budgets from different departments).
- **Mini Project**: Merge 3 different CSV files (e.g., HR, Sales, Marketing budgets) into a single dataset.
        """
    },
    16: {
        "title": "Day 16: Automate Excel Report Generation",
        "content": """
- **Overview**: Use Python to create or update Excel reports (e.g., using `openpyxl` or `xlsxwriter`).
- **Mini Project**: Write a script to generate a daily/weekly report and format it nicely in Excel.
        """
    },
    17: {
        "title": "Day 17: Do Statistical Analysis",
        "content": """
- **Overview**: Perform descriptive statistics, hypothesis testing, or basic trend analysis on finance data.
- **Mini Project**: Calculate the mean, median, standard deviation of monthly sales data. 
        """
    },
    18: {
        "title": "Day 18: Retrieve Stock Data using yfinance",
        "content": """
- **Overview**: Practice pulling real-time or historical financial data with `yfinance`.
- **Mini Project**: Fetch stock data for a chosen ticker and plot its closing price trend.
        """
    },
    19: {
        "title": "Day 19: Intro to Machine Learning for Forecasting",
        "content": """
- **Overview**: Gain familiarity with basic ML concepts using `scikit-learn`.
- **Mini Project**: Create a simple regression model to predict monthly revenue based on historical data.
        """
    },
    20: {
        "title": "Day 20: Creating a Linear Regression Model",
        "content": """
- **Overview**: Dive deeper into linear regression, coefficients, intercepts, and evaluation metrics (MSE, R^2).
- **Mini Project**: Build a linear regression to predict daily sales based on marketing spend.
        """
    },
    21: {
        "title": "Day 21: Clustering & Segmentation",
        "content": """
- **Overview**: Learn unsupervised learning (K-means or hierarchical clustering).
- **Mini Project**: Cluster different product lines based on profitability or usage data.
        """
    },
    22: {
        "title": "Day 22: Using ARIMA for Time Series Forecasting",
        "content": """
- **Overview**: Forecast monthly sales or revenue data using an ARIMA model.
- **Mini Project**: Fit an ARIMA model on sample time-series data and generate future predictions.
        """
    },
    23: {
        "title": "Day 23: Prophet for Forecasting",
        "content": """
- **Overview**: Explore Facebook's Prophet library for quick, intuitive time series forecasting.
- **Mini Project**: Use Prophet on monthly sales or cost data to forecast the next 6-12 months.
        """
    },
    24: {
        "title": "Day 24: Building a Predictive Model Pipeline",
        "content": """
- **Overview**: Combine data cleaning, feature engineering, and model training into one pipeline.
- **Mini Project**: Automate your forecasting steps so that new data can be easily fed into the model.
        """
    },
    25: {
        "title": "Day 25: Automate Email Generation",
        "content": """
- **Overview**: Write a script that automatically sends out performance or forecast summaries via email.
- **Mini Project**: Build a script that compiles the daily forecast results into an email body and sends it.
        """
    },
    26: {
        "title": "Day 26: Automate Slides Generation",
        "content": """
- **Overview**: Programmatically create presentations (e.g., with Python-PPTX) for stakeholder updates.
- **Mini Project**: Use Python to generate a simple deck with charts and bullet points from your data.
        """
    },
    27: {
        "title": "Day 27: Automate a Discounted Cash Flow Model",
        "content": """
- **Overview**: Write a script that calculates Net Present Value (NPV), Internal Rate of Return (IRR) automatically.
- **Mini Project**: Create a DCF model for a hypothetical project, produce NPV and IRR outputs.
        """
    },
    28: {
        "title": "Day 28: Learn About Jupyter Notebooks & Anaconda",
        "content": """
- **Overview**: Explore the Jupyter ecosystem, environment management, and best practices for data science.
- **Mini Project**: Set up a new environment in Anaconda, install libraries, and run a financial analysis notebook.
        """
    },
    29: {
        "title": "Day 29: Practice, Integrate, and Review",
        "content": """
- **Overview**: Integrate all your learnings: data import, cleaning, visualization, automation, forecasting, etc.
- **Mini Project**: Create a short end-to-end project that reads data, cleans it, does a small forecast, and prints a summary.
        """
    },
    30: {
        "title": "Day 30: Final Capstone Project",
        "content": """
- **Overview**: Consolidate everything into a final project that includes data visualization, automation, and forecasting.
- **Mini Project**: Build a fully automated FP&A mini-dashboard with scripts for data cleaning, analysis, forecasting, and emailing the results.
        """
    },
}

def main():
    st.title("30 Days to Master Python for FP&A")
    st.write(
        """
        This interactive guide is based on the Path to Master Python by Christian Martinez & Nicolas Boucher.
        Each day includes a brief overview of what to learn plus a mini project to sharpen your skills.
        """
    )

    # Let user pick a day in the sidebar
    day = st.sidebar.selectbox("Select a day to view details", list(days_plan.keys()))

    st.header(days_plan[day]["title"])
    st.write(days_plan[day]["content"])


if __name__ == "__main__":
    main()
