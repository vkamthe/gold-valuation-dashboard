# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

A single-page, static dashboard analyzing **50+ years of Gold Valuation metrics in USD (1971 – 2026)**.
Compares spot gold prices against money supply expansion, shadow reserve backing, real inflation-adjusted purchasing power, and cross-asset commodity ratios.

## Architecture

- **`index.html`** — Self-contained dashboard built with vanilla HTML/CSS and Chart.js. Reads `data/data.json` dynamically on page load.
- **`fetch.py`** — Data aggregator script. Fetches real-time price quotes (Gold `GC=F`, Silver `SI=F`, Oil `CL=F`, S&P 500 `^GSPC`) via `yfinance` and updates `data/data.json`.
- **`data/data.json`** — Combined dataset containing 50-year monthly historical metrics and current live prices.
- **`.github/workflows/update.yml`** — Daily GitHub Action workflow to fetch updated prices and auto-commit `data/data.json` to redeploy GitHub Pages.

## Local Preview

```bash
python3 -m http.server 8000
# Open http://localhost:8000
```

## Running the Data Fetcher

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python fetch.py
```
