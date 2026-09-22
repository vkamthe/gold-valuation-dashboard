# Gold Valuation Dashboard (1971 – 2026)

An interactive, 50-year macroeconomic valuation dashboard for Gold in USD. Built with **vanilla HTML5/CSS, Chart.js, Python, and GitHub Actions**.

---

## 🌟 Features & Metrics

1. **Gold Market Cap / US M2 Money Supply (%)**: Tracks paper currency debasement against total above-ground gold stock (212,500 metric tonnes).
2. **Shadow Gold Price ($/oz)**: Calculates the price per ounce required if US Official Gold Reserves (261.5M oz) were to 100% back US M2 money supply.
3. **Real Inflation-Adjusted Gold Price**: Adjusts historical gold prices to 2026 constant dollars using US CPI.
4. **Cross-Asset Commodity Ratios**: Gold-to-Silver Ratio (GSR) and Gold-to-Oil Ratio (barrels per oz).
5. **50-Year Interactive Time Series Charts**: Full 1971–2026 interactive multi-axis charting powered by Chart.js.

---

## 🛠 Local Development & Testing

To run and preview the dashboard on your local machine:

```bash
# 1. Preview the web app
python3 -m http.server 8000
# Open http://localhost:8000 in your browser

# 2. Re-run the data aggregator
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/python fetch.py
```

---

## 🚀 How to Publish for Free on GitHub Pages

Follow these simple steps to deploy your dashboard online:

### Step 1: Initialize Git & Push to GitHub

Create a new repository on GitHub (name it `gold-valuation-dashboard`), then run the following in your terminal:

```bash
cd /Users/vikramkamthe/projects/gold-valuation-dashboard
git init
git add .
git commit -m "Initial commit: 50-year Gold Valuation Dashboard"
git branch -M main
git remote add origin https://github.com/<your-github-username>/gold-valuation-dashboard.git
git push -u origin main
```
*(Replace `<your-github-username>` with your actual GitHub username).*

---

### Step 2: Enable GitHub Pages

1. Go to your repo on GitHub: `https://github.com/<your-github-username>/gold-valuation-dashboard`.
2. Click **Settings** $\rightarrow$ **Pages** (in the left sidebar).
3. Under **Build and deployment**:
   - **Source**: Select `Deploy from a branch`.
   - **Branch**: Select `main` and folder `/ (root)`.
4. Click **Save**.
5. Within 1–2 minutes, your website will be live at:
   `https://<your-github-username>.github.io/gold-valuation-dashboard/`

---

### Step 3: Enable Daily Auto-Updates (GitHub Actions)

1. On your GitHub repo, click **Settings** $\rightarrow$ **Actions** $\rightarrow$ **General**.
2. Scroll down to **Workflow permissions**.
3. Select **Read and write permissions**.
4. Click **Save**.

Now, every weekday after market close, GitHub Actions will automatically run `fetch.py` and keep your gold valuation dashboard updated with zero server costs!

---

## 📜 License
MIT License. Free to use, modify, and share.
