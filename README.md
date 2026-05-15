# Financial Portfolio Analysis Dashboard

## Project Overview
End-to-end financial analytics project analyzing a 10-stock portfolio 
from 2020-2024 using Python, SQL, Power BI, and Tableau Cloud.

## Live Dashboard
- Tableau Dashboard: [View Here]([YOUR_TABLEAU_LINK_HERE](https://prod-in-a.online.tableau.com/#/site/bhumivarshney7017-098db6f5b4/home))

## Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn, SciPy)
- SQL (SQLite) | Power BI | Tableau Cloud | Excel | yfinance API

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
- Best performer: TSLA (~45% annualized return)
- Best risk-adjusted: MSFT (Sharpe Ratio 1.15)
- Most stable: JNJ (lowest volatility ~16%)
- COVID crash detected via Z-score analysis (March 2020)
- Tech stocks showed highest correlation with each other

## Statistical Metrics
- Annualized Return and Volatility
- Sharpe Ratio (risk-adjusted return)
- Beta (market sensitivity vs S&P 500)
- Value at Risk (95% confidence)
- Z-score anomaly detection
- Pearson correlation matrix

## Project Structure
financial-dashboard/
├── scripts/         # Python scripts
├── data/processed/  # Cleaned datasets
├── reports/         # Excel reports and charts
├── dashboards/      # Power BI .pbix file
└── requirements.txt # Dependencies

## How to Run
1. Clone the repo
2. pip install -r requirements.txt
3. Run scripts/powerbi_export.py
4. Open Power BI dashboard
