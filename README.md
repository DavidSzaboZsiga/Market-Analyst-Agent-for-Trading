# 📈 AI Market Intelligence Analyst

A local, autonomous Python agent that acts as your personal quantitative analyst. It connects to live market data, reads the latest news, and synthesizes a strategic trading briefing based on your custom "Risk DNA."

Built with **Python**, **LangGraph**, **OpenAI GPT-4o**, and **Tavily AI Search**.

## 🚀 Features

* **Multi-Agent Architecture:** Runs specialized agents (Quant, News, Analyst) in parallel for maximum speed.
* **Live Market Data:** Fetches real-time price, volume, and momentum data using `yfinance`.
* **AI News Filtering:** Uses GPT-4o to filter out "market noise" and identify genuine catalyst events.
* **Customizable Strategy:** Define your own "Strategy DNA" (e.g., Aggressive Growth, Value, Day Trader) to change how the agent interprets data.
* **Local Execution:** Runs entirely on your machine; no data is sent to third-party SaaS platforms (other than the LLM/Search providers).

## 🛠️ Architecture

The agent follows a **State Graph** workflow:

Start --> Quant_Agent[📊 Quant Agent]

Quant_Agent -->|Passes Price Data| News_Agent[📰 News Hunter]

News_Agent -->|Passes News & Sentiment| Manager[💼 Portfolio Manager]

Manager -->|Generates Report| End

## 📋 Prerequisites

* **Python 3.10 or higher**

* **OpenAI API Key (for the Brain)**

* **Tavily API Key (for the Browsing)**

## Installation

**1. Clone the repository (or download the files):**
```
git clone https://github.com/DavidSzaboZsiga/Market-Analyst-Agent-for-Trading.git
cd market-agent
```

**2. Create a Virtual Environment:**
```
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

**3. Install Dependencies:**
```
pip install -r requirements.txt
```

**4. Configure API Keys:**
Create a `.env` file in the root directory:
```
touch .env
```

Add your keys:
```
OPENAI_API_KEY=sk-proj-...
TAVILY_API_KEY=tvly-...
```

## 🏃 Usage

**1. Edit your Watchlist:**
Open `config.py` and modify the `WATCHLIST` variable:
```
WATCHLIST = ["NVDA", "BTC-USD", "TSLA"]
```

**2. Run the Agent:**
```
python main.py
```

**3. View Results:**
The agent will print the report to the terminal and save a `market_brief.md` file in the project folder.

## 🧠 Customizing the "Brain"

You can change the agent's personality by editing `STRATEGY_DNA` in `config.py`.

*Example: The Conservative Investor*
```
STRATEGY_DNA = """
You are a conservative wealth manager.
- Focus on: Dividends, cash flow, and capital preservation.
- Ignore: Hype, crypto volatility, and speculative tech.
- Verdicts: Be skeptical of any rally without earnings support.
"""
```

## ⚠️ Disclaimer

**This project is for educational purposes only.**