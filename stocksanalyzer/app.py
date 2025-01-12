import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Streamlit app title
st.title("Stock Market Visualizer")

# Sidebar for stock selection and configurations
st.sidebar.header("Stock Selection")
selected_stock = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT):", "AAPL")
start_date = st.sidebar.date_input("Start Date:", datetime(2020, 1, 1))
end_date = st.sidebar.date_input("End Date:", datetime.now())

# Fetch stock data using yfinance
def fetch_stock_data(ticker, start, end):
    try:
        stock_data = yf.download(ticker, start=start, end=end)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Fetch and display stock data
st.sidebar.header("Visualizations")
show_candlestick = st.sidebar.checkbox("Show Candlestick Chart", True)
show_moving_averages = st.sidebar.checkbox("Add Moving Averages", False)
ma_periods = st.sidebar.slider("Select MA Period:", min_value=5, max_value=100, value=20) if show_moving_averages else None

stock_data = fetch_stock_data(selected_stock, start_date, end_date)

if stock_data is not None and not stock_data.empty:
    st.subheader(f"Stock Data for {selected_stock} ({start_date} to {end_date})")
    st.write(stock_data.tail())

    # Plot candlestick chart
    if show_candlestick:
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=stock_data.index,
            open=stock_data['Open'],
            high=stock_data['High'],
            low=stock_data['Low'],
            close=stock_data['Close'],
            name="Candlestick"
        ))

        # Add moving average overlay
        if show_moving_averages:
            stock_data[f"MA_{ma_periods}"] = stock_data['Close'].rolling(window=ma_periods).mean()
            fig.add_trace(go.Scatter(
                x=stock_data.index,
                y=stock_data[f"MA_{ma_periods}"],
                mode='lines',
                name=f"MA_{ma_periods}"
            ))

        # Customize layout
        fig.update_layout(
            title=f"Candlestick Chart for {selected_stock}",
            xaxis_title="Date",
            yaxis_title="Price",
            template="plotly_white"
        )

        st.plotly_chart(fig)

    # Portfolio tracking: CSV/Excel upload
    st.sidebar.header("Portfolio Tracking")
    uploaded_file = st.sidebar.file_uploader("Upload Portfolio (CSV/Excel):")
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                portfolio_data = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                portfolio_data = pd.read_excel(uploaded_file)
            else:
                st.error("Please upload a CSV or Excel file.")

            st.subheader("Uploaded Portfolio")
            st.write(portfolio_data)

        except Exception as e:
            st.error(f"Error loading file: {e}")

    # Exporting charts
    st.sidebar.header("Export Options")
    export_as_png = st.sidebar.button("Export Chart as PNG")
    export_as_html = st.sidebar.button("Export Chart as HTML")

    if export_as_png or export_as_html:
        file_name = f"{selected_stock}_chart"
        if export_as_png:
            fig.write_image(f"{file_name}.png")
            st.success(f"Chart exported as {file_name}.png")

        if export_as_html:
            fig.write_html(f"{file_name}.html")
            st.success(f"Chart exported as {file_name}.html")

else:
    st.warning("No data available for the selected stock and date range.")

# Save configurations for sharing
st.sidebar.header("Save Configurations")
save_config = st.sidebar.button("Save Config")
if save_config:
    config = {
        "selected_stock": selected_stock,
        "start_date": start_date.strftime('%Y-%m-%d'),
        "end_date": end_date.strftime('%Y-%m-%d'),
        "show_candlestick": show_candlestick,
        "show_moving_averages": show_moving_averages,
        "ma_periods": ma_periods,
    }
    with open("config.json", "w") as f:
        import json
        json.dump(config, f)
    st.success("Configuration saved as config.json")

# GitHub integration instructions
st.sidebar.header("Version Control")
st.sidebar.write("Push your code to GitHub using Streamlit's Git integration.")
st.sidebar.write("Follow [Streamlit GitHub Guide](https://docs.streamlit.io/library/advanced-features/version-control).")
