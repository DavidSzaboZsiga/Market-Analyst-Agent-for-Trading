import asyncio
from graph import app
from config import WATCHLIST

async def main():
    print("Starting Market Research Agent...")
    
    initial_state = {
        "tickers": WATCHLIST,
        "market_data": {},
        "news_analysis": [],
        "final_report": ""
    }
    
    result = await app.ainvoke(initial_state)
    
    print("\n\n" + "="*50)
    print("DAILY TRADING BRIEFING")
    print("="*50 + "\n")
    print(result["final_report"])
    
    # Save to file
    with open("market_brief.md", "w") as f:
        f.write(result["final_report"])

if __name__ == "__main__":
    asyncio.run(main())