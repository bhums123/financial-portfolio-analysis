"""
Data utilities for financial dashboard
"""
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from config import MA_SHORT, MA_MEDIUM, MA_LONG

def fetch_multiple_stocks(tickers, days=365):
    """Fetch data for multiple stock tickers"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    data = {}
    for ticker in tickers:
        try:
            data[ticker] = yf.download(ticker, start=start_date, end=end_date, progress=False)
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")
    
    return data

def calculate_technical_indicators(df):
    """Calculate technical indicators"""
    df = df.copy()
    
    # Moving Averages
    df['MA_20'] = df['Adj Close'].rolling(window=MA_SHORT).mean()
    df['MA_50'] = df['Adj Close'].rolling(window=MA_MEDIUM).mean()
    df['MA_200'] = df['Adj Close'].rolling(window=MA_LONG).mean()
    
    # Returns
    df['Daily_Return'] = df['Adj Close'].pct_change()
    df['Cumulative_Return'] = (1 + df['Daily_Return']).cumprod() - 1
    
    # Volatility (20-day rolling)
    df['Volatility'] = df['Daily_Return'].rolling(window=20).std()
    
    # RSI (14-day)
    df['RSI'] = calculate_rsi(df['Adj Close'])
    
    return df

def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index"""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_stock_summary(ticker, days=365):
    """Get summary statistics for a stock"""
    data = yf.download(ticker, period=f"{days}d", progress=False)
    data = calculate_technical_indicators(data)
    
    return {
        'ticker': ticker,
        'current_price': data['Adj Close'].iloc[-1],
        'high_52w': data['Adj Close'].max(),
        'low_52w': data['Adj Close'].min(),
        'avg_daily_return': data['Daily_Return'].mean(),
        'volatility': data['Daily_Return'].std(),
        'ma_20': data['MA_20'].iloc[-1],
        'ma_50': data['MA_50'].iloc[-1],
        'rsi': data['RSI'].iloc[-1]
    }
