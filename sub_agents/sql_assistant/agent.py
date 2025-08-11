from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search

SQLQueryGen = """
You are an expert in SQL query generation. Follow below instructions while working with Columns
1. Remove special chars with underscore
2. Use CAPS for column and table names
3. Abbrevations: Date with DT, Timestamp with TS, Description with DESC,Number with NO
4. Ensure data type is compatible with MS Fabric - https://learn.microsoft.com/en-us/fabric/data-warehouse/data-types
5. Arrange related columns in a logical order
"""

root_agent = Agent(
    name="sql_assistant",
    model="gemini-2.0-flash",
    description="Agent to assist users in upgrading their Databricks Runtime (DBR) versions by coordinating with sub-agents.",
    instruction=SQLQueryGen,
    tools=[google_search],
)   