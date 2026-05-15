"""
Financial Dashboard Configuration
"""

# Stock tickers to track
DEFAULT_TICKERS = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

# Time periods (in days)
SHORT_TERM = 30
MEDIUM_TERM = 90
LONG_TERM = 365

# Moving average windows
MA_SHORT = 20
MA_MEDIUM = 50
MA_LONG = 200

# Database settings
DATABASE_URL = "sqlite:///financial_data.db"

# Chart settings
CHART_STYLE = "darkgrid"
CHART_DPI = 100
CHART_FIGSIZE = (14, 6)
