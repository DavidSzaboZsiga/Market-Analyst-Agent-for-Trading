import operator
from typing import Annotated, List, TypedDict, Dict, Any

class AgentState(TypedDict):
    tickers: List[str]
    market_data: Annotated[Dict[str, Any], lambda x, y: {**x, **y}] # Merges dicts
    news_analysis: Annotated[List[str], operator.add]
    final_report: str