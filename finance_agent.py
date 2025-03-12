from phi.agent import Agent
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
import openai


import os
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")

finance_agent = Agent(
    name="Finance Agent",
        model=OpenAIChat(id="gpt-4"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)
finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)