from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
     model = Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["include source link"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
     model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
     model = Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("give the analysis of NVDA and news for MSFT", stream=True)