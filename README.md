# Gold Valuation Dashboard (1971 – 2026)

An interactive 50-year macroeconomic valuation dashboard for Gold in USD. Built with **vanilla HTML5/CSS, Chart.js, Python, and GitHub Actions**.

---

## 🌟 3 Core Metrics & Paired 50-Year Charts

1. **Gold Market Cap vs. US M2 Money Supply (%)**: Measures paper currency debasement by comparing global gold market cap to total US M2 money supply.
2. **Nominal vs. Inflation-Adjusted (Real) Gold Price**: Strips out 50+ years of US CPI inflation to evaluate gold's true purchasing power in constant 2026 USD terms.
3. **Precious Metals & Commodity Ratios**: Cross-asset purchasing power metrics tracking Gold-to-Silver Ratio (GSR) and Gold-to-Oil Ratio (barrels per oz).

---

## 🔄 Update Schedule & Automation

- **Automated Execution**: Updates automatically every weekday at **22:00 UTC (18:30 IST / post-US market close)** via GitHub Actions.
- **Data Pipeline**: Runs `fetch.py` using `yfinance` to pull live prices for Gold (`GC=F`), Silver (`SI=F`), Oil (`CL=F`), and S&P 500 (`^GSPC`), regenerating `data/data.json`.

---

## 🛠 Local Development & Testing

```bash
# 1. Preview locally
python3 -m http.server 8000
# Open http://localhost:8000 in your browser

# 2. Re-run data fetcher
./venv/bin/python fetch.py
```

---

## 🌐 Live Website
👉 **[https://vkamthe.github.io/gold-valuation-dashboard/](https://vkamthe.github.io/gold-valuation-dashboard/)**
