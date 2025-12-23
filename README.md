# 📈 Stock Return Prediction Using Supervised Learning

## Overview
This project implements an **end-to-end supervised machine learning pipeline** to study whether short-term stock price movements can be predicted using historical price and volume data.

The objective is **not** to build a profitable trading system, but to:
- design a correct ML pipeline
- work with real-world financial data
- understand the limitations of linear models in noisy markets

---

## Data Source
- Daily OHLCV stock data
- Fetched using `yfinance` (Yahoo Finance API wrapper)
- Universe: large-cap Indian stocks (NIFTY constituents)
- Time span: ~5 years of historical data

---

## Feature Engineering

Each stock is processed independently to avoid data leakage.

### Features used:
- 1-day return
- 5-day return
- 10-day return
- 5-day rolling volatility
- 20-day rolling volatility
- Volume ratio (current volume / recent average)
- Volume change rate

All features use **only past information**.

---

## Modeling (Baseline Experiment)

### Task
- **Regression**
- Predict **next-day return**

### Model
- Linear Regression (scikit-learn)

### Evaluation Metrics
- MAE
- MSE
- RMSE

### Results
The model achieves weak predictive performance, with error magnitudes comparable to typical daily market movements.

This result is **expected** and consistent with the Efficient Market Hypothesis.  
No data leakage or artificial performance inflation is present.

---

## Key Learnings
- Correct data pipelines matter more than model complexity
- Financial time series are extremely noisy
- Handling NaNs, infinities, headers, and dtypes is unavoidable
- Honest evaluation is more important than impressive metrics

---

## Planned Improvement

### Problem Reframing
The regression task will be reframed as a **classification problem**.

Instead of predicting return magnitude, the model will predict:
- **1** → next-day price goes up
- **0** → next-day price goes down or stays flat

### Motivation
- Direction is often more predictable than magnitude
- Clearer evaluation (accuracy, precision, recall)
- Same feature pipeline can be reused
- Reflects common real-world financial ML setups

This change will be implemented as a **clean extension**, not a rewrite.

---

## Disclaimer
This project is for educational purposes only and does not constitute financial or trading advice.
All datasets are generated programmatically and are excluded from version control.
