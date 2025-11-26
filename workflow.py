"""Workflow orchestration for the research agent system."""
from google.adk.agents import SequentialAgent, ParallelAgent
from agents import (
    create_tech_researcher,
    create_health_researcher,
    create_finance_researcher,
    create_aggregator_agent
)


def create_research_workflow() -> SequentialAgent:
    """Create the complete research workflow.
    
    Returns:
        SequentialAgent: The root agent that orchestrates the entire workflow.
    """
    # Create individual research agents
    tech_researcher = create_tech_researcher()
    health_researcher = create_health_researcher()
    finance_researcher = create_finance_researcher()
    aggregator_agent = create_aggregator_agent()
    
    # Create parallel research team
    parallel_research_team = ParallelAgent(
        name="ParallelResearchTeam",
        sub_agents=[tech_researcher, health_researcher, finance_researcher],
    )
    
    # Create sequential workflow: parallel research then aggregation
    root_agent = SequentialAgent(
        name="ResearchSystem",
        sub_agents=[parallel_research_team, aggregator_agent],
    )
    
    print("✅ Parallel and Sequential Agents created.")
    return root_agent
