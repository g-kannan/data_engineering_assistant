from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search
from sql_assistant.prompt import SQLAssistantPrompt
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

root_agent = Agent(
    name="sql_assistant",
    model="gemini-2.0-flash",
    description="Agent to assist users in upgrading their Databricks Runtime (DBR) versions by coordinating with sub-agents.",
    instruction=SQLAssistantPrompt,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="uvx",
                args=[
                        "mcp-server-motherduck",
                        "--db-path",
                        ":memory:"
                    ]
            )
        ),
    ],
)   