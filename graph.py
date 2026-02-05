from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import market_data_node, news_node, report_node

workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("quant_analyst", market_data_node)
workflow.add_node("news_analyst", news_node)
workflow.add_node("portfolio_manager", report_node)

# Flow:
# 1. Start -> Get Hard Data (Quant)
# 2. Quant -> Get News (News Analyst)
# 3. News -> Write Report (Manager)
workflow.set_entry_point("quant_analyst")
workflow.add_edge("quant_analyst", "news_analyst")
workflow.add_edge("news_analyst", "portfolio_manager")
workflow.add_edge("portfolio_manager", END)

app = workflow.compile()