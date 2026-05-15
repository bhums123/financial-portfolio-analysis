# Financial Portfolio Analysis Dashboard

## Project Overview
End-to-end financial analytics project analyzing a 10-stock portfolio 
from 2020-2024 using Python, SQL, Power BI, and Tableau Cloud.

## Live Dashboard
- Tableau Dashboard: [View Here](YOUR_TABLEAU_LINK)

## Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)
- SQL (SQLite)
- Power BI Desktop
- Tableau Cloud
- Excel (openpyxl)
- yfinance API

## Stocks Analyzed
| Stock | Ticker | Sector |
|-------|--------|--------|
| Apple | AAPL | Technology |
| Microsoft | MSFT | Technology |
| JPMorgan | JPM | Finance |
| Goldman Sachs | GS | Finance |
| Johnson & Johnson | JNJ | Healthcare |
| Pfizer | PFE | Healthcare |
| Tesla | TSLA | EV/Auto |
| ExxonMobil | XOM | Energy |
| Amazon | AMZN | E-Commerce |
| Infosys | INFY | IT Services |

## Key Findings
- Best performer: TSLA with highest annualized return (~45%)
- Best risk-adjusted return: MSFT with Sharpe Ratio of 1.15
- Most stable stock: JNJ with lowest volatility (~16%)
- COVID crash detected via Z-score anomaly detection (March 2020)
- Tech stocks (AAPL, MSFT, AMZN) showed highest correlation

## Statistical Metrics Calculated
- Annualized Return and Volatility
- Sharpe Ratio (risk-adjusted return)
- Beta (market sensitivity vs S&P 500)
- Value at Risk at 95% confidence
- Z-score anomaly detection
- Pearson correlation matrix

## Project Structure
financial-dashboard/
├── scripts/            # Python scripts
├── data/processed/     # Cleaned datasets
├── reports/            # Excel reports and charts
├── dashboards/         # Power BI .pbix file
└── requirements.txt    # Dependencies

## How to Run
1. Clone the repo
2. pip install -r requirements.txt
3. Run scripts/powerbi_export.py
4. Open Power BI dashboard
