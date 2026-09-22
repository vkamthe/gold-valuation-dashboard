# Gold Valuation Dashboard (1971 – 2026)

An interactive 50-year macroeconomic valuation dashboard for Gold in USD. Built with **vanilla HTML5/CSS, Chart.js, Python, and GitHub Actions**.

---

## 🌟 Features & Metrics

1. **Gold Market Cap / US M2 Money Supply (%)**: Tracks paper currency debasement against total above-ground gold stock (212,500 metric tonnes).
2. **Central Bank Net Buying & Reserve Allocation**: Tracks annual net central bank gold purchases (tonnes/year) and gold as a % of global foreign exchange reserves.
3. **Real Inflation-Adjusted Gold Price**: Adjusts historical gold prices to 2026 constant dollars using US CPI.
4. **Cross-Asset Commodity Ratios**: Gold-to-Silver Ratio (GSR) and Gold-to-Oil Ratio (barrels per oz).
5. **Dates on All Current Prices**: Displays exact price observation dates across all metrics.

---

## 🔄 Update Schedule & Automation

- **Automated Execution**: The dashboard updates automatically every weekday at **22:00 UTC (18:30 IST / post-US market close)** via GitHub Actions.
- **Data Pipeline**: Runs `fetch.py` using `yfinance` to pull live prices for Gold (`GC=F`), Silver (`SI=F`), Oil (`CL=F`), and S&P 500 (`^GSPC`), regenerating `data/data.json`.

---

## 🛠 Local Development & Testing

```bash
# 1. Preview locally
python3 -m http.server 8000
# Open http://localhost:8000 in your browser

# 2. Re-run the data aggregator
./venv/bin/python fetch.py
```

---

## 🌐 Live Website
👉 **[https://vkamthe.github.io/gold-valuation-dashboard/](https://vkamthe.github.io/gold-valuation-dashboard/)**
