# Financial Dashboard

A Python-based financial dashboard for tracking and analyzing stock market data.

## Features

- **Real-time Stock Data**: Fetch historical stock prices using yfinance
- **Technical Analysis**: Calculate moving averages, RSI, volatility, and returns
- **Visualization**: Create interactive charts with matplotlib and seaborn
- **Multi-stock Support**: Track multiple stocks simultaneously
- **Data Storage**: SQLite database integration for storing historical data

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from app import fetch_stock_data, calculate_metrics, plot_stock_chart

# Fetch data
data = fetch_stock_data("AAPL")

# Calculate metrics
data = calculate_metrics(data)

# Plot chart
plot_stock_chart(data, "AAPL")
```

### Using Data Utilities

```python
from data_utils import get_stock_summary

# Get summary for a stock
summary = get_stock_summary("GOOGL", days=365)
print(summary)
```

## Project Structure

```
financial-dashboard/
├── app.py              # Main application
├── config.py           # Configuration settings
├── data_utils.py       # Data utility functions
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dependencies

- yfinance: Download stock market data
- pandas: Data manipulation and analysis
- numpy: Numerical computations
- matplotlib: Data visualization
- seaborn: Statistical data visualization
- scipy: Scientific computing
- sqlalchemy: Database ORM
- jupyter: Interactive notebooks

## Technical Indicators

- **Moving Averages**: 20-day, 50-day, 200-day
- **RSI**: 14-day Relative Strength Index
- **Volatility**: 20-day rolling standard deviation
- **Returns**: Daily and cumulative returns

## Future Enhancements

- Web interface with Flask/Streamlit
- Real-time data streaming
- Portfolio management
- Advanced charting with plotly
- Email alerts for price changes
- Machine learning predictions

## License

MIT License
