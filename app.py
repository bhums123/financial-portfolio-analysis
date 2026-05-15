import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set style
sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 6)

def fetch_stock_data(ticker, days=365):
    """Fetch historical stock data"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    return data

def calculate_metrics(data):
    """Calculate key financial metrics"""
    data['Daily_Return'] = data['Adj Close'].pct_change()
    data['MA_20'] = data['Adj Close'].rolling(window=20).mean()
    data['MA_50'] = data['Adj Close'].rolling(window=50).mean()
    
    return data

def plot_stock_chart(data, ticker):
    """Plot stock price with moving averages"""
    plt.figure(figsize=(14, 6))
    plt.plot(data.index, data['Adj Close'], label='Close Price', linewidth=2)
    plt.plot(data.index, data['MA_20'], label='20-day MA', linewidth=1.5, alpha=0.7)
    plt.plot(data.index, data['MA_50'], label='50-day MA', linewidth=1.5, alpha=0.7)
    
    plt.title(f'{ticker} Stock Price', fontsize=16, fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

def main():
    """Main dashboard function"""
    ticker = "AAPL"
    
    print(f"Fetching data for {ticker}...")
    data = fetch_stock_data(ticker)
    
    # Check if data was fetched successfully
    if data.empty:
        print(f"Error: No data available for {ticker}. Check internet connection or ticker symbol.")
        return
    
    print("Calculating metrics...")
    data = calculate_metrics(data)
    
    # Display summary statistics
    print("\n" + "="*50)
    print(f"{ticker} Summary Statistics (1 Year)")
    print("="*50)
    print(f"Current Price: ${data['Adj Close'].iloc[-1]:.2f}")
    print(f"52-Week High: ${data['Adj Close'].max():.2f}")
    print(f"52-Week Low: ${data['Adj Close'].min():.2f}")
    print(f"Average Daily Return: {data['Daily_Return'].mean():.4f} ({data['Daily_Return'].mean()*100:.2f}%)")
    print(f"Volatility (Std Dev): {data['Daily_Return'].std():.4f} ({data['Daily_Return'].std()*100:.2f}%)")
    print("="*50)
    
    # Plot the chart
    plot_stock_chart(data, ticker)

if __name__ == "__main__":
    main()
