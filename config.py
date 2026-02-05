import os
from dotenv import load_dotenv

load_dotenv()

# Your Portfolio
# Add the assets you hold or want to watch
#WATCHLIST = ["NVDA", "TSLA", "BTC-USD", "AAPL"]
WATCHLIST = ["VTI", "VOO", "GOOGL", "AAPL", "META", "MSFT"]

# --- Brand/Strategy DNA ---
STRATEGY_DNA = """
You are a ruthless hedge fund analyst. 
- Focus on: Catalyst events (earnings, regulatory changes, product launches).
- Ignore: Generic market fluff, celebrity gossip, or minor price fluctuations.
- Risk Tolerance: Medium. Look for asymmetric upside.
"""