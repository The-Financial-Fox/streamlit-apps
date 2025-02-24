import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd

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

# Inject custom SEO metadata into the app
components.html(
    """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Learn Python for Finance in 30 Days</title>
        <meta name="description" content="This is our path for you to learn Python">
        <meta property="og:title" content="Python for Finance">
        <meta property="og:description" content="Learn Python and its applications in finance in 30 days.">
        <meta property="og:image" content="https://example.com/path-to-your-image.jpg">
        <meta property="og:url" content="https://pythonfinancelearningpath.streamlit.app">
        <meta name="twitter:card" content="summary_large_image">
    </head>
    </html>
    """,
    height=0  # Set height to 0 so it doesn't show extra space
)
days_plan = {
    1: {
        "title": "Day 1: Getting Started with Python & Google Colab",
        "content": """
**Overview**  
- Learn how to set up a Google Colab notebook to write and run basic Python code.  
- Get introduced to common Python tools used in Finance.  

**Step-by-Step**  
1. **Create a Google Account**: If you don’t already have one, sign up at [accounts.google.com](https://accounts.google.com).  
2. **Open Google Colab**: Go to [colab.research.google.com](https://colab.research.google.com).  
3. **Create a New Notebook**: Click on `New Notebook`.  
4. **Basic Python Syntax**:  
   - Printing statements: `print("Hello, FP&A World!")`  
   - Variables:  
     ```python
     revenue = 1000
     expenses = 400
     profit = revenue - expenses
     print("Profit =", profit)
     ```
   - Simple arithmetic: `2 + 2`, `10 * 5`, `100 / 10`.

**Why Python for Finance?**  
- **Automation**: Python can automate routine tasks like merging Excel files, generating reports, or scraping financial data.  
- **Analysis & Modeling**: Libraries like `pandas` and `numpy` make it easy to handle large datasets, while tools like `scikit-learn` or `Prophet` help with forecasting.  
- **Visualization**: Libraries such as `matplotlib`, `seaborn`, and `plotly` help turn data into insights.

**Mini Project**  
1. **Hello FP&A World**: In your new Colab notebook, write a simple `print("Hello, FP&A World!")`.  
2. **Basic Arithmetic**: Create two variables, `revenue` and `expenses`. Subtract them to find `profit`. Play around by changing their values and printing the results.  
3. **Reflection**: Write short comments in your notebook about how this could be used in a real FP&A scenario (e.g., tracking daily, weekly, or monthly numbers).  

**Additional Resources**  
- [Google Colab Official Guide](https://colab.research.google.com/notebooks/intro.ipynb)  
- [10 Ways to Use Python for Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_how-to-use-python-for-fpa-by-christian-martinez-activity-7275419452328837120-9cYD?utm_source=share&utm_medium=member_desktop) (for quick Python refreshers)  
- [Python in Excel Guide](https://nicolasboucher.online/product/python-in-excel-guide/)

This is the Full Path by Christian Martinez & Nicolas Boucher

![Python Path](https://raw.githubusercontent.com/The-Financial-Fox/streamlit-apps/main/pathpython/pythonpath.jpg)

"""
    },
    
    # The rest of the days remain as they were
    2: {
        "title": "Day 2: Handling Your First Python Errors",
        "content": """
**Overview**  
- Learn about common Python error messages (SyntaxError, NameError, TypeError, etc.).
- Practice asking ChatGPT or using search engines for help in debugging.

**Step-by-Step**  
1. **Intentional Errors**: Write a few lines of code that produce different errors (e.g., missing parenthesis, misspelled variable name).  
2. **Debugging**: For each error, see what the traceback says. Google the error message or ask ChatGPT to get tips on fixing it.  
3. **Basic Fixes**: Once you know how to fix the error, modify your code and run it again.  

**Mini Project**  
- **“Error Buffet” Notebook**: Create a Colab notebook called `day2_errors.ipynb` and deliberately introduce:  
  1. A **SyntaxError** (e.g., missing a `:` or parenthesis).  
  2. A **NameError** (calling a variable that doesn’t exist).  
  3. A **TypeError** (trying to add a string and an integer).  
- Write down how you **debugged** each one.  

**Additional Resources**  
- [Python for FP&A and Finance ](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-fpa-and-finance-activity-7160885608951803905-2QY9?utm_source=share&utm_medium=member_desktop)  
- [Python for Beginners / Finance ](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-beginners-finance-activity-7176841429363642368-fCW_?utm_source=share&utm_medium=member_desktop)  
- [A Simple Guide of Python for Finance ](https://www.linkedin.com/posts/christianmartinezthefinancialfox_a-simple-guide-of-python-for-finance-by-christian-activity-7062293000357384192-m-Lv?utm_source=share&utm_medium=member_desktop)  
- [Python with ChatGPT for Finance ](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-with-chatgpt-for-finance-activity-7218853994020880384-xY8L?utm_source=share&utm_medium=member_desktop)  
"""
    },

    3: {
        "title": "Day 3: ChatGPT for Generating Python Code",
        "content": """
**Overview**  
- Explore how to leverage ChatGPT to scaffold simple scripts and solve coding challenges for finance.
- Learn to prompt ChatGPT effectively: providing clear context, specifying inputs/outputs, etc.

**Step-by-Step**  
1. **Intro to Prompt Engineering**:  
   - Be specific about what you want ChatGPT to generate.  
   - Provide examples of input data and desired output.  
2. **Ask ChatGPT for a Starter Script**:  
   - Example: “ChatGPT, generate a Python script that calculates and prints the monthly budget surplus or deficit.”  
3. **Iterate**:  
   - If the script is missing something, refine your prompt with more details.  

**Mini Project**  
- **Budget Calculator**:  
  1. Use ChatGPT to generate a simple script that asks for user input (`monthly_income`, `monthly_expenses`) and outputs the difference.  
  2. Copy/paste that generated code into Colab or a `.py` file and run it.  
  3. Document any modifications you made to the ChatGPT output.  

**Additional Resources**  
- [Python for FP&A and Finance (LinkedIn Post)](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-fpa-and-finance-activity-7160885608951803905-2QY9?utm_source=share&utm_medium=member_desktop)  
- [Python for Beginners / Finance (LinkedIn Post)](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-beginners-finance-activity-7176841429363642368-fCW_?utm_source=share&utm_medium=member_desktop)  
- [A Simple Guide of Python for Finance (LinkedIn Post)](https://www.linkedin.com/posts/christianmartinezthefinancialfox_a-simple-guide-of-python-for-finance-by-christian-activity-7062293000357384192-m-Lv?utm_source=share&utm_medium=member_desktop)  
- [Python with ChatGPT for Finance (LinkedIn Post)](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-with-chatgpt-for-finance-activity-7218853994020880384-xY8L?utm_source=share&utm_medium=member_desktop)  
"""
    },
    4: {
        "title": "Day 4: Using Python Libraries for Finance",
        "content": """
**Overview**  
- Learn about the core libraries every FP&A professional should know: **pandas**, **numpy**, **yfinance**, etc.
- Understand how these libraries can streamline data analysis, automate tasks, and improve reporting.

**Step-by-Step**  
1. **pandas**:
   - Great for tabular data (think “Excel in Python”).
   - Common operations: reading CSV/Excel, data manipulation with `DataFrame`.
2. **numpy**:
   - Offers fast array operations and numerous mathematical functions.
   - Frequently used under the hood by pandas.
3. **yfinance**:
   - Designed for retrieving historical market data from Yahoo Finance (stock prices, volume, etc.).
   - Great for building dashboards or running quick portfolio analyses.
4. **Also Explore** (from the 7 recommended libraries for FP&A):
   - **openpyxl** or **xlsxwriter** to create/update Excel files programmatically.
   - **requests** or **BeautifulSoup** (web scraping if you need to grab financial data online).
   - **plotly** or **matplotlib** for data visualization.

**Mini Project**  
- **Check Stock Data**:  
  1. Install or import `yfinance`.  
  2. Fetch historical data for a stock (e.g., AAPL) for the last 6 months.  
  3. Save the data to a CSV using `pandas`.  
  4. Generate a quick line plot of the stock’s closing prices.

**Additional Resources**  
- [7 Python Libraries I Believe Every FP&A Professional Should Master (LinkedIn)](https://www.linkedin.com/posts/christianmartinezthefinancialfox_7-python-libraries-i-believe-every-fpa-professional-activity-7232248897786564608-5A5x?utm_source=share&utm_medium=member_desktop)
- [Python for FP&A and Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-fpa-and-finance-activity-7160885608951803905-2QY9?utm_source=share&utm_medium=member_desktop)
- [Python for Beginners / Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-beginners-finance-activity-7176841429363642368-fCW_?utm_source=share&utm_medium=member_desktop)
- [A Simple Guide of Python for Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_a-simple-guide-of-python-for-finance-by-christian-activity-7062293000357384192-m-Lv?utm_source=share&utm_medium=member_desktop)
- [Python with ChatGPT for Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-with-chatgpt-for-finance-activity-7218853994020880384-xY8L?utm_source=share&utm_medium=member_desktop)

![Python Libraries](https://raw.githubusercontent.com/The-Financial-Fox/streamlit-apps/main/pathpython/Python_Libraries.png)

        
        """
        
    },

    5: {
        "title": "Day 5: Adding Data into Your Python Environment",
        "content": """
**Overview**  
- Dive deeper into ways to import data: from local files, Google Drive, CSV, Excel, or even APIs.
- Understand best practices for file organization and environment management.

**Step-by-Step**  
1. **Local Files**:
   - Use `pandas.read_csv("my_data.csv")` or `pandas.read_excel("my_data.xlsx")`.
   - Make sure your file path is correct (upload to Colab or set a working directory if local).
2. **Google Drive Integration** (Colab):
   - Mount your Drive in Colab:  
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```
   - Once mounted, you can read files from `/content/drive/MyDrive/...`.
3. **APIs & Web Sources**:
   - Tools like `requests` can help retrieve data from APIs or websites.
   - After fetching, convert the raw data into a pandas DataFrame.
4. **Excel Nuances**:
   - If your data is in multiple sheets, use `sheet_name` parameter in `read_excel`.
   - If you need advanced formatting, look into libraries like **openpyxl** or **xlsxwriter**.

**Mini Project**  
1. **CSV + Excel Merge**:
   - Download or create two files: one CSV and one Excel with financial data.
   - Load both into Python using `pandas`.
   - Combine them (e.g., `pd.concat` or `pd.merge`) into a single DataFrame.
   - Print out the first few rows to confirm.
2. **Reflect**: 
   - If you had to do this manually every month, how much time would it take?
   - Write a short note in your notebook on how Python can automate this.

"""
    },
    6: {
        "title": "Day 6: Python as a Pivot Table",
        "content": """
**Overview**  
- Learn how to replicate Excel-like pivot table functionality using Python’s `pandas`.
- Use grouping, aggregating, and pivot techniques to summarize financial data (sales, expenses, budget vs. actuals).

**Step-by-Step**  
1. **Load a Dataset**:  
   - Use `pandas.read_csv("your_financial_data.csv")` (or `.read_excel()`).  
2. **Group By & Aggregation**:  
   - Example: `df.groupby("Region")["Revenue"].sum()` to get total revenue by region.
   - Combine multiple fields:  
     ```python
     df.groupby(["Region", "Product"])[["Revenue", "Expenses"]].sum()
     ```
3. **Pivot Tables**:  
   - Use `pandas.pivot_table(df, index="Region", columns="Product", values="Revenue", aggfunc="sum")`
   - Try different `aggfunc` values like `"mean"`, `"count"`, or a custom function.
4. **Formatting & Insights**:  
   - Sort values, rename columns, or export the result to a new Excel file.

**Mini Project**  
- **Pivot Table Challenge**:  
  1. Load a dataset with columns like `Region`, `Month`, `Revenue`, `Expenses`.  
  2. Use `groupby` or `pivot_table` to find total revenue and expenses by month and by region.  
  3. Print or export your summarized data to verify.  

"""
    },

    7: {
        "title": "Day 7: Simple Bar Chart in Python",
        "content": """
**Overview**  
- Explore fundamental data visualization techniques in Python using libraries like **matplotlib**, **seaborn**, or **plotly**.
- Learn how to create a bar chart to compare categories (e.g., monthly revenue, expenses, or product sales).

**Step-by-Step**  
1. **Install Matplotlib**: If you're using Colab, run `!pip install matplotlib` in a code cell.  
2. **Basic Bar Chart**:  
   ```python
   import matplotlib.pyplot as plt

   months = ["January", "February", "March", "April"]
   revenue = [1000, 1500, 1200, 1700]

   plt.bar(months, revenue)
   plt.title("Monthly Revenue")
   plt.xlabel("Month")
   plt.ylabel("Revenue in USD")
   plt.show()

   
Styling & Seaborn:
You can do sns.barplot(x="Month", y="Revenue", data=df) for a quick bar chart.
Customize color, labels, figure size, etc.
Compare Two Series (optional):
Plot revenue and expenses side by side, or use a stacked bar chart to see them together.
Mini Project

Revenue vs. Expenses Bar Chart:
Create a small dataset with Month, Revenue, and Expenses.
Plot them on a single bar chart or two separate subplots.
Label everything clearly and draw a quick conclusion (Which month had the highest net profit?).


""" },
  8: {
        "title": "Day 8: Seaborn Library Essentials",
        "content": """
**Overview**  
- Learn how to create visually appealing charts with **Seaborn**, which provides a high-level interface for drawing attractive statistical graphics.
- Explore Seaborn’s built-in themes, color palettes, and advanced chart types to uncover insights in FP&A data.

**Step-by-Step**  
1. **Install & Import**  
   - If needed, install in Colab/terminal: `!pip install seaborn`.
   - Import:  
     ```python
     import pandas as pd
     import seaborn as sns
     import matplotlib.pyplot as plt
     ```
   - Optionally set a style for Seaborn:
     ```python
     sns.set_style("whitegrid")
     ```
2. **Load Your Data**  
   - Example: A CSV with columns like `Month`, `Region`, `Revenue`, `Expenses`.
   - `df = pd.read_csv("financial_data.csv")`
3. **Create a Basic Chart**  
   - **Barplot** (for categorical data):
     ```python
     sns.barplot(x="Month", y="Revenue", data=df)
     plt.title("Monthly Revenue")
     plt.show()
     ```
   - **Line Plot** (trends over time):
     ```python
     sns.lineplot(x="Month", y="Revenue", data=df, marker="o")
     plt.title("Revenue Trend")
     plt.show()
     ```
4. **Distribution & Box Plots**  
   - Distribution plot for `Revenue`:
     ```python
     sns.histplot(df["Revenue"], kde=True)
     plt.title("Distribution of Revenue")
     plt.show()
     ```
   - Box plot comparing `Revenue` by `Region`:
     ```python
     sns.boxplot(x="Region", y="Revenue", data=df)
     plt.title("Revenue by Region")
     plt.show()
     ```
5. **Customization**  
   - Adjust figure size:  
     ```python
     plt.figure(figsize=(10,6))
     ```
   - Change color palettes:  
     ```python
     sns.set_palette("viridis")  # or "Blues", "coolwarm", etc.
     ```

**Mini Project**  
1. **Deep Dive into Seaborn**:
   - Pick a finance dataset (e.g., monthly or quarterly data).
   - Create at least **three** different plot types (bar, line, box, histogram, etc.).
   - Experiment with **styling** (custom palettes, figure sizes).
2. **Analysis**:
   - Summarize which visual best communicates key insights (e.g., outliers, trends, comparisons).

**Additional Resources**  
- [Seaborn Official Documentation](https://seaborn.pydata.org/)  
- [Matplotlib vs. Seaborn (Comparison)](https://www.geeksforgeeks.org/differences-between-seaborn-and-matplotlib/)  
- [Kaggle Datasets](https://www.kaggle.com/datasets) (for extra practice data)  
      """
    },
  9: {
    "title": "Day 9: Box Plot for Statistical Analysis",
    "content": """
- **Overview**: Box plots (also known as box-and-whisker plots) provide a visual representation of data distribution. They help identify the median, quartiles, and potential outliers in a dataset. Understanding box plots is essential for detecting anomalies and gaining insights into financial or operational data.

- **Step-by-Step**:
  1. **Introduction to Box Plots**: A box plot consists of:
     - **Box**: Spans the interquartile range (IQR), showing the 25th to the 75th percentiles.
     - **Median Line**: The line inside the box, representing the 50th percentile.
     - **Whiskers**: Extend to the smallest and largest values within 1.5 * IQR.
     - **Outliers**: Points outside the whiskers.
  2. **Prepare Your Data**: Use a financial dataset (e.g., monthly sales, expenses, or revenue). Ensure the data is in a clean format (e.g., a CSV file or a DataFrame).
  3. **Plot a Box Plot in Python**:

- **Code Example**:
```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Sample financial dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [1200, 1100, 1300, 1150, 1400, 1250]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a box plot using Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['Revenue'])
plt.title("Monthly Revenue Distribution")
plt.ylabel("Revenue ($)")
plt.show()
```

- **Interpretation**:
  - Analyze the box plot:
    - Check the median to understand central tendencies.
    - Look for outliers (points outside the whiskers).
    - Examine the spread of the box to assess variability.

- **Mini Project**:
  1. Use your own data (e.g., budget, sales, or expenses).
  2. Plot a box plot to analyze outliers and trends.
  3. Write a short report on:
     - Any anomalies you identified.
     - How these insights could influence decisions (e.g., handling outliers).

- **Additional Resources**:
  - [Box Plots Explained](https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51)
  - [Seaborn Box Plot Documentation](https://seaborn.pydata.org/generated/seaborn.boxplot.html)
  - [Using Python for Financial Analytics](https://www.analyticsvidhya.com/blog/2020/01/finance-analytics-python/)
"""

    },
10: {
    "title": "Day 10: Correlation Analysis with Heatmap",
    "content": """
- **Overview**: 
  Gain insights into the relationships between financial variables by computing correlations and visualizing them using heatmaps. Learn to identify strong, weak, positive, and negative correlations to support data-driven decision-making.

- **Key Objectives**:
  1. Understand the concept of correlation and its significance in financial analysis.
  2. Learn to calculate correlation coefficients using Python.
  3. Create and interpret heatmaps for visualizing correlations effectively.

- **Steps and Code Samples**:
  1. **Load the Dataset**:
     Start by loading a sample financial dataset (e.g., stock prices, sales data, or economic indicators).
     ```python
     import pandas as pd
     import seaborn as sns
     import matplotlib.pyplot as plt

     # Load dataset
     data = pd.read_csv('financial_data.csv')
     print(data.head())
     ```

  2. **Compute Correlation Matrix**:
     Calculate the correlation matrix to analyze relationships between numerical variables.
     ```python
     correlation_matrix = data.corr()
     print(correlation_matrix)
     ```

  3. **Visualize with Heatmap**:
     Use the `seaborn` library to create a heatmap for a clear visualization of the correlation matrix.
     ```python
     plt.figure(figsize=(10, 8))
     sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
     plt.title('Correlation Heatmap')
     plt.show()
     ```

  4. **Interpret Results**:
     - Identify highly correlated variables (e.g., close to +1 or -1).
     - Note potential multicollinearity in predictors for regression models.
     - Use insights to guide financial strategy or data preprocessing.

- **Mini Project**:
  1. Use a financial dataset, such as historical stock prices or company KPIs.
  2. Compute correlations among variables like revenue, profit, expense, or stock returns.
  3. Create a detailed heatmap and write a brief analysis of key findings, such as:
     - Which variables are highly correlated?
     - Are there surprising or unexpected relationships?
     - How can these insights improve forecasting or decision-making?

- **Additional Resources**:
  - [Seaborn Heatmap Documentation](https://seaborn.pydata.org/generated/seaborn.heatmap.html)
  - [Understanding Correlation in Finance](https://example-finance-correlation.com)

"""

    },
 11: {
    "title": "Day 11: Customizing Any Data Visualization",
    "content": """
- **Overview**: Adjust labels, colors, legends, and style to build compelling dashboards.
- **Mini Project**: Take a bar chart or line chart and fully customize it (title, axis labels, color palette).

# Detailed Instructions:

## Learning Goals:
1. Understand the importance of effective visualizations for financial data.
2. Learn how to use Python libraries such as Matplotlib and Seaborn to enhance plots.
3. Develop skills to tailor charts for specific audiences (e.g., executives vs. analysts).

## Steps:
1. **Set Up Your Environment**:
    - Install required libraries: `pip install matplotlib seaborn pandas`
    - Import necessary modules:
      ```python
      import matplotlib.pyplot as plt
      import seaborn as sns
      import pandas as pd
      ```

2. **Choose a Dataset**:
    - Use a financial dataset (e.g., revenue, profit, expenses over time).
    - Example:
      ```python
      data = {
          'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
          'Revenue': [20000, 25000, 22000, 27000],
          'Expenses': [15000, 18000, 16000, 19000]
      }
      df = pd.DataFrame(data)
      ```

3. **Create a Basic Plot**:
    - Start with a simple line chart:
      ```python
      plt.plot(df['Month'], df['Revenue'], label='Revenue')
      plt.plot(df['Month'], df['Expenses'], label='Expenses')
      ```

4. **Add Customizations**:
    - Title and labels:
      ```python
      plt.title('Monthly Financial Overview', fontsize=16)
      plt.xlabel('Month', fontsize=12)
      plt.ylabel('Amount ($)', fontsize=12)
      ```
    - Customize colors and styles:
      ```python
      sns.set_style('whitegrid')
      plt.plot(df['Month'], df['Revenue'], color='green', linestyle='--', marker='o')
      plt.plot(df['Month'], df['Expenses'], color='red', linestyle='-', marker='x')
      ```
    - Add a legend:
      ```python
      plt.legend(loc='upper left')
      ```

5. **Enhance for Dashboards**:
    - Annotate points with exact values:
      ```python
      for i, val in enumerate(df['Revenue']):
          plt.text(df['Month'][i], val, f"{val}", ha='center', va='bottom', fontsize=10)
      ```
    - Adjust layout for readability:
      ```python
      plt.tight_layout()
      ```

6. **Save and Share**:
    - Save your plot for presentations:
      ```python
      plt.savefig('financial_overview.png', dpi=300)
      ```
    - Show the plot:
      ```python
      plt.show()
      ```

## Stretch Goals:
- Use Seaborn to create a heatmap of financial metrics.
- Experiment with interactive libraries like Plotly for enhanced interactivity.
- Add comparison benchmarks or trend lines.

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

    # 1) Create a list of “Day 1”, “Day 2”, etc.
    day_options = [f"Day {day_num}" for day_num in days_plan.keys()]
    
    # 2) Put the selectbox in the main area (NOT in the sidebar)
    selected_label = st.selectbox("Select a day to view details", day_options)
    
    # 3) Convert the selected label back to an integer key (e.g., "Day 1" → 1)
    #    We assume the label format is "Day X", so split and parse:
    selected_day = int(selected_label.split()[1])
    
    # 4) Display content
    st.header(days_plan[selected_day]["title"])
    st.write(days_plan[selected_day]["content"])

if __name__ == "__main__":
    main()
