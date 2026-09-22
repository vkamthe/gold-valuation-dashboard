#!/usr/bin/env python3
"""
Gold Valuation Data Fetcher & Aggregator
-----------------------------------------
Fetches live market data (via yfinance) and merges it with historical macroeconomic
series (M2, CPI, US Debt, Central Bank Purchases, Equities, Silver, Oil).

Output: data/data.json
"""

import os
import json
import datetime
import yfinance as yf

# Constants for Gold Calculations
TOTAL_ABOVE_GROUND_OZ = 6.832e9  # ~212,500 metric tonnes in troy ounces

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DATA_FILE = os.path.join(DATA_DIR, "data.json")
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

def generate_historical_series():
    """Generates benchmark data points from 1971 to 2026."""
    raw_benchmarks = [
        # date, gold_nom, cpi, m2_billions, sp500, silver, oil, us_debt_trillion, real_yield_pct, cb_net_buying_tonnes, cb_reserve_pct
        ("1971-01", 38.0, 39.8, 630, 93.5, 1.60, 3.60, 0.40, 2.5, 200, 68.0),
        ("1973-01", 65.0, 42.6, 760, 118.0, 2.00, 4.50, 0.45, 1.8, 150, 65.0),
        ("1975-01", 175.0, 52.1, 980, 72.5, 4.40, 11.50, 0.53, -1.2, 0, 60.0),
        ("1977-01", 132.0, 58.5, 1170, 107.0, 4.30, 13.90, 0.67, 1.0, -50, 62.0),
        ("1979-01", 226.0, 68.3, 1370, 99.7, 6.00, 14.80, 0.82, 0.5, -100, 69.0),
        ("1980-01", 675.0, 77.8, 1490, 114.2, 36.00, 39.50, 0.91, -2.5, -150, 72.0),
        ("1982-01", 380.0, 94.3, 1750, 117.3, 8.10, 34.00, 1.14, 5.2, -180, 58.0),
        ("1984-01", 370.0, 101.9, 2140, 166.4, 8.60, 29.50, 1.56, 6.5, -200, 52.0),
        ("1986-01", 345.0, 109.6, 2570, 208.4, 6.10, 15.00, 2.13, 4.8, -220, 45.0),
        ("1988-01", 447.0, 115.7, 2870, 250.5, 6.70, 17.10, 2.60, 4.2, -250, 40.0),
        ("1990-01", 410.0, 127.4, 3160, 339.9, 5.20, 22.80, 3.23, 3.8, -300, 32.0),
        ("1992-01", 355.0, 138.1, 3370, 417.1, 4.10, 18.70, 4.06, 3.1, -400, 25.0),
        ("1994-01", 387.0, 146.2, 3480, 472.0, 5.20, 15.00, 4.69, 3.5, -420, 20.0),
        ("1996-01", 398.0, 154.4, 3640, 615.9, 5.50, 18.10, 5.22, 3.7, -450, 18.0),
        ("1998-01", 289.0, 161.6, 4030, 970.4, 5.90, 14.40, 5.55, 3.9, -520, 15.0),
        ("1999-08", 256.0, 167.1, 4520, 1320.0, 5.10, 20.00, 5.65, 4.1, -550, 13.0),
        ("2000-01", 283.0, 168.8, 4670, 1455.2, 5.30, 27.20, 5.68, 4.3, -480, 13.5),
        ("2002-01", 287.0, 177.1, 5450, 1148.1, 4.50, 19.40, 6.00, 3.2, -540, 11.5),
        ("2004-01", 415.0, 185.2, 6070, 1131.1, 6.20, 34.30, 7.10, 2.1, -470, 10.2),
        ("2006-01", 545.0, 198.3, 6680, 1278.7, 9.00, 65.50, 8.40, 2.3, -360, 9.5),
        ("2008-01", 889.0, 211.0, 7490, 1447.2, 16.10, 92.90, 9.40, 1.6, -230, 9.8),
        ("2009-03", 920.0, 212.7, 8310, 735.1, 13.10, 48.00, 11.10, 1.8, -30, 10.1),
        ("2010-12", 1410.0, 219.2, 8800, 1257.6, 30.90, 91.40, 13.50, 1.0, 79, 10.8),
        ("2011-09", 1820.0, 226.6, 9540, 1218.9, 40.10, 89.00, 14.80, -0.8, 457, 12.1),
        ("2013-01", 1670.0, 230.3, 10430, 1472.1, 31.40, 94.70, 16.40, -0.6, 623, 11.4),
        ("2015-12", 1060.0, 236.5, 12300, 2043.9, 14.00, 37.00, 18.90, 0.7, 589, 9.6),
        ("2017-01", 1200.0, 242.8, 13270, 2275.1, 17.00, 52.50, 19.90, 0.4, 379, 10.4),
        ("2019-01", 1290.0, 251.7, 14440, 2607.4, 15.60, 51.40, 21.90, 0.9, 668, 11.8),
        ("2020-08", 2040.0, 259.9, 18350, 3373.4, 27.10, 42.30, 26.50, -1.0, 273, 13.5),
        ("2022-01", 1815.0, 281.1, 21650, 4577.1, 23.10, 83.20, 30.00, -0.8, 1082, 15.2), # Record buying
        ("2023-01", 1890.0, 299.2, 21380, 3999.1, 23.80, 78.10, 31.40, 1.2, 1037, 16.4),
        ("2024-01", 2040.0, 308.4, 20780, 4769.8, 23.10, 73.80, 34.10, 1.8, 1040, 17.5),
        ("2024-10", 2740.0, 315.7, 21210, 5815.0, 33.80, 71.50, 35.80, 1.9, 1060, 18.0),
        ("2025-06", 3350.0, 318.5, 21500, 5950.0, 36.20, 68.00, 36.20, 1.7, 1090, 18.3),
        ("2026-09", 4400.0, 322.0, 21800, 6000.0, 41.50, 72.00, 36.80, 1.6, 1120, 18.6)
    ]

    latest_cpi = raw_benchmarks[-1][2]
    series = []

    for item in raw_benchmarks:
        d, g_nom, cpi, m2_b, sp500, sil, oil, debt_t, ry, cb_buy, cb_res_pct = item
        
        gold_mkt_cap_b = (TOTAL_ABOVE_GROUND_OZ * g_nom) / 1e9
        gold_m2_pct = round((gold_mkt_cap_b / m2_b) * 100, 2)
        real_gold = round(g_nom * (latest_cpi / cpi), 2)
        
        gsr = round(g_nom / sil, 2) if sil > 0 else None
        gor = round(g_nom / oil, 2) if oil > 0 else None

        series.append({
            "date": d,
            "gold_nominal": g_nom,
            "gold_real": real_gold,
            "cpi": cpi,
            "m2_billions": m2_b,
            "gold_mkt_cap_billions": round(gold_mkt_cap_b, 2),
            "gold_m2_pct": gold_m2_pct,
            "sp500": sp500,
            "silver": sil,
            "oil": oil,
            "gsr": gsr,
            "gor": gor,
            "us_debt_trillions": debt_t,
            "real_yield": ry,
            "cb_net_buying_tonnes": cb_buy,
            "cb_reserve_pct": cb_res_pct
        })
    
    return series


def fetch_live_data():
    """Fetches real-time price updates for Gold, Silver, Oil, S&P 500 from yfinance."""
    tickers = {
        "gold": "GC=F",
        "silver": "SI=F",
        "oil": "CL=F",
        "sp500": "^GSPC",
        "tnx": "^TNX",
        "dxy": "DX-Y.NYB"
    }
    
    fetched = {}
    for name, sym in tickers.items():
        try:
            df = yf.Ticker(sym).history(period="5d")["Close"].dropna()
            if len(df) > 0:
                fetched[name] = float(df.iloc[-1])
        except Exception as e:
            print(f"Warning: Failed to fetch {name} ({sym}): {e}")
            
    return fetched


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    now_ist = datetime.datetime.now(IST)
    
    # 1. Historical time series
    series = generate_historical_series()
    
    # 2. Live fetch update
    live = fetch_live_data()
    
    latest_gold = live.get("gold", series[-1]["gold_nominal"])
    latest_silver = live.get("silver", series[-1]["silver"])
    latest_oil = live.get("oil", series[-1]["oil"])
    latest_sp500 = live.get("sp500", series[-1]["sp500"])
    
    # Update last record with live prices
    series[-1]["gold_nominal"] = round(latest_gold, 2)
    series[-1]["silver"] = round(latest_silver, 2)
    series[-1]["oil"] = round(latest_oil, 2)
    series[-1]["sp500"] = round(latest_sp500, 2)
    
    # Re-calculate latest derived metrics
    g_mkt_cap_b = (TOTAL_ABOVE_GROUND_OZ * latest_gold) / 1e9
    m2_latest = series[-1]["m2_billions"]
    gold_m2_pct = round((g_mkt_cap_b / m2_latest) * 100, 2)
    gsr = round(latest_gold / latest_silver, 2) if latest_silver > 0 else None
    gor = round(latest_gold / latest_oil, 2) if latest_oil > 0 else None
    
    series[-1]["gold_mkt_cap_billions"] = round(g_mkt_cap_b, 2)
    series[-1]["gold_m2_pct"] = gold_m2_pct
    series[-1]["gsr"] = gsr
    series[-1]["gor"] = gor

    current_date_str = now_ist.strftime("%d %b %Y")
    updated_timestamp = now_ist.strftime("%d %b %Y %H:%M IST")

    output = {
        "updated": updated_timestamp,
        "latest": {
            "date": current_date_str,
            "gold_price": round(latest_gold, 2),
            "gold_mkt_cap_trillion": round(g_mkt_cap_b / 1000.0, 2),
            "gold_m2_pct": gold_m2_pct,
            "real_gold_price_2026_usd": series[-1]["gold_real"],
            "gsr": gsr,
            "gor": gor,
            "m2_trillion": round(m2_latest / 1000.0, 2),
            "us_debt_trillion": series[-1]["us_debt_trillions"],
            "real_yield_pct": series[-1]["real_yield"],
            "cb_net_buying_tonnes": series[-1]["cb_net_buying_tonnes"],
            "cb_reserve_pct": series[-1]["cb_reserve_pct"]
        },
        "benchmarks": {
            "historical_m2_peak_1980_pct": 100.0,
            "historical_m2_trough_2000_pct": 15.0,
            "historical_gsr_mean": 62.5,
            "historical_gor_mean": 18.0
        },
        "series": series
    }

    with open(DATA_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Successfully generated {DATA_FILE} at {updated_timestamp}")
    print(f"Gold Spot: ${latest_gold:.2f}/oz | Date: {current_date_str} | Gold/M2: {gold_m2_pct}% | CB Buying: +{series[-1]['cb_net_buying_tonnes']} tonnes/yr")


if __name__ == "__main__":
    main()
