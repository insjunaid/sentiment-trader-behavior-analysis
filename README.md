# Market Sentiment vs Trader Behavior Analysis

## Objective

This project analyzes how Bitcoin market sentiment (Fear/Greed) influences trader behavior and performance on Hyperliquid.

The goal is to identify behavioral patterns, regime-dependent performance shifts, and extract actionable trading insights.

---

## Datasets Used

1. Bitcoin Fear/Greed Index
2. Hyperliquid Historical Trader Data

---

## Methodology

### 1. Data Preparation
- Cleaned and standardized datasets
- Converted timestamps to daily format
- Merged trader data with sentiment regime
- Removed unmatched sentiment rows

### 2. Feature Engineering
- Daily PnL per trader
- Trade frequency
- Position size segmentation
- Win rate calculation
- Long/Short bias
- Consistency segmentation (PnL volatility proxy)

### 3. Regime Analysis
Compared:
- Mean & median PnL across regimes
- Trade size behavior shifts
- Frequency behavior shifts
- Volatility differences

### 4. Trader Segmentation
Segmented traders into:
- Large vs Small size
- Frequent vs Infrequent
- Consistent vs Inconsistent

Clustered traders using KMeans into behavioral archetypes.

### 5. Predictive Modeling (Bonus)
Built a Random Forest model to predict:
- Next-day trader profitability (Accuracy: ~61.7%)
- Rolling volatility (risk proxy)

---

## Key Insights

- Profitability increases during extreme sentiment regimes.
- Larger position sizes capture disproportionate returns.
- Infrequent traders outperform frequent traders during Greed.
- High-PnL traders rely on asymmetric payoff structures rather than high win rates.

---

## Strategy Recommendations

### Rule 1: Regime-Based Capital Scaling
- Increase exposure during Extreme Fear & Greed.
- Reduce risk during Neutral regimes.
- Allocate capital toward high-performing size segments.

### Rule 2: Avoid Overtrading During Greed
- Frequent traders underperform in Greed regimes.
- Favor selective, high-conviction setups.

---

## Streamlit Dashboard

A lightweight interactive dashboard was built using Streamlit to explore:

- PnL distributions
- Trade size behavior
- Trade frequency
- Summary statistics

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-trader-behavior-analysis.git
cd sentiment-trader-behavior-analysis

### 2. Create Virtual Environment
```bash
python -m venv venv

### 3. Activate Environment
Windows

```bash
venv\Scripts\activate

Mac/Linux

```bash
source venv/bin/activate

### 4. Install Dependencies
```bash
pip install -r requirements.txt

### 5. Run Dashboard
```bash
streamlit run app.py

---

## Project Structure
sentiment-trader-behavior-analysis/
│
├── sentiment_trader_behavior_analysis.ipynb
├── app.py
├── merged_data.csv
├── requirements.txt
├── README.md

---

## Conclusion

- This analysis demonstrates that market sentiment materially influences trader behavior and performance.