import os
import yfinance as yf
import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from tavily import TavilyClient
from config import STRATEGY_DNA
from state import AgentState
from dotenv import load_dotenv

llm = ChatOpenAI(model="gpt-4o", temperature=0)
tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# Node 1: The Quantitative Analyst (Hard Data)
def market_data_node(state: AgentState):
    tickers = state["tickers"]
    data_summary = {}
    
    print(f"--- Fetching Market Data for: {tickers} ---")
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="5d") # Last 5 days
        
        # Calculate simple momentum
        current_price = hist["Close"].iloc[-1]
        start_price = hist["Close"].iloc[0]
        pct_change = ((current_price - start_price) / start_price) * 100
        
        data_summary[ticker] = {
            "current_price": round(current_price, 2),
            "5d_change_pct": round(pct_change, 2),
            "volume_avg": int(hist["Volume"].mean())
        }
    
    return {"market_data": data_summary}

# Node 2: The News Hunter (Soft Data)
async def news_node(state: AgentState):
    tickers = state["tickers"]
    print(f"--- Searching News for: {tickers} ---")
    
    analysis_results = []
    
    async def analyze_ticker(ticker):
        # 1. Get News
        query = f"latest news and analysis for {ticker} stock market reason for movement"
        search_result = await asyncio.to_thread(tavily.search, query=query, topic="news", days=3)
        context = "\n".join([r["content"] for r in search_result["results"][:3]])
        
        # 2. Analyze Sentiment (The "Relevance Filter" from the video)
        prompt = (
            f"Ticker: {ticker}\n"
            f"Strategy DNA: {STRATEGY_DNA}\n"
            f"News Snippets:\n{context}\n\n"
            "Summarize the KEY reason for this stock's recent movement in 2 sentences. "
            "If it's just noise, say 'No significant catalyst'."
        )
        response = llm.invoke([HumanMessage(content=prompt)])
        return f"**{ticker}**: {response.content}"

    # Run in parallel
    results = await asyncio.gather(*(analyze_ticker(t) for t in tickers))
    return {"news_analysis": results}

# Node 3: The Portfolio Manager (Decision Maker)
def report_node(state: AgentState):
    print("--- Writing Final Strategy Report ---")
    
    # Combine Data + News
    financials = state["market_data"]
    news = "\n".join(state["news_analysis"])
    
    prompt = (
        f"You are a Portfolio Manager using this Strategy DNA: {STRATEGY_DNA}\n\n"
        f"MARKET DATA:\n{financials}\n\n"
        f"NEWS INTELLIGENCE:\n{news}\n\n"
        "Task: Write a daily trading briefing. "
        "For each asset, give a verdict (BULLISH / BEARISH / NEUTRAL) and explain why based on the data and news. "
        "Flag any high-risk warnings."
    )
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"final_report": response.content}