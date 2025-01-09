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

**Additional Resources**  
- [7 Python Libraries I Believe Every FP&A Professional Should Master (LinkedIn)](https://www.linkedin.com/posts/christianmartinezthefinancialfox_7-python-libraries-i-believe-every-fpa-professional-activity-7232248897786564608-5A5x?utm_source=share&utm_medium=member_desktop)
- [Python for FP&A and Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-fpa-and-finance-activity-7160885608951803905-2QY9?utm_source=share&utm_medium=member_desktop)
- [Python for Beginners / Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-for-beginners-finance-activity-7176841429363642368-fCW_?utm_source=share&utm_medium=member_desktop)
- [A Simple Guide of Python for Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_a-simple-guide-of-python-for-finance-by-christian-activity-7062293000357384192-m-Lv?utm_source=share&utm_medium=member_desktop)
- [Python with ChatGPT for Finance](https://www.linkedin.com/posts/christianmartinezthefinancialfox_python-with-chatgpt-for-finance-activity-7218853994020880384-xY8L?utm_source=share&utm_medium=member_desktop)
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
