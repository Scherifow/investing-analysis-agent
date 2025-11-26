"""Research agents for different domains."""
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from config import GOOGLE_API_KEY, RETRY_CONFIG, MODEL_NAME


def create_tech_researcher() -> Agent:
    """Create the Technology Research Agent.
    
    Focuses on AI and ML trends.
    """
    agent = Agent(
        name="TechResearcher",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction="""Research the latest AI/ML trends. Include 3 key developments,
the main companies involved, and the potential impact. Keep the report very concise (100 words).""",
        tools=[google_search],
        output_key="tech_research",
    )
    print("✅ tech_researcher created.")
    return agent


def create_health_researcher() -> Agent:
    """Create the Health Research Agent.
    
    Focuses on medical breakthroughs.
    """
    agent = Agent(
        name="HealthResearcher",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction="""Research recent medical breakthroughs. Include 3 significant advances,
their practical applications, and estimated timelines. Keep the report concise (100 words).""",
        tools=[google_search],
        output_key="health_research",
    )
    print("✅ health_researcher created.")
    return agent


def create_finance_researcher() -> Agent:
    """Create the Finance Research Agent.
    
    Focuses on fintech trends.
    """
    agent = Agent(
        name="FinanceResearcher",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction="""Research current fintech trends. Include 3 key trends,
their market implications, and the future outlook. Keep the report concise (100 words).""",
        tools=[google_search],
        output_key="finance_research",
    )
    print("✅ finance_researcher created.")
    return agent


def create_aggregator_agent() -> Agent:
    """Create the Aggregator Agent.
    
    Synthesizes results from all research agents into an executive summary.
    """
    agent = Agent(
        name="AggregatorAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction="""Combine these three research findings into a single executive summary:

    **Technology Trends:**
    {tech_research}
    
    **Health Breakthroughs:**
    {health_research}
    
    **Finance Innovations:**
    {finance_research}
    
    Your summary should highlight common themes, surprising connections, and the most important key takeaways from all three reports. The final summary should be around 200 words.""",
        output_key="executive_summary",
    )
    print("✅ aggregator_agent created.")
    return agent
