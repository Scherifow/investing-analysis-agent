"""Workflow orchestration for the investment analysis agent system."""
from google.adk.agents import SequentialAgent, ParallelAgent
from agents import (
    create_business_understanding_agent,
    create_competitive_advantage_agent,
    create_media_sentiment_agent,
    create_ethics_agent,
    create_investment_horizon_agent,
    create_insider_trading_agent,
    create_google_trends_agent,
    create_share_dilution_agent,
    create_short_interest_agent,
    create_debt_analysis_agent,
    create_infinite_game_agent,
    create_ceo_analysis_agent,
    create_analyst_ratings_agent,
    create_technical_analysis_agent,
    create_reverse_analysis_agent,
    create_bond_correlation_agent,
    create_investment_aggregator
)


def create_research_workflow(stock_query: str) -> SequentialAgent:
    """Create the complete investment analysis workflow.
    
    Args:
        stock_query: The stock ticker or company name to analyze.
    
    Returns:
        SequentialAgent: The root agent that orchestrates the entire workflow.
    """
    print(f"🔧 Creating investment analysis agents for {stock_query}...")
    
    # Create all analysis agents with stock_query
    business_agent = create_business_understanding_agent(stock_query)
    competitive_agent = create_competitive_advantage_agent(stock_query)
    media_agent = create_media_sentiment_agent(stock_query)
    ethics_agent = create_ethics_agent(stock_query)
    horizon_agent = create_investment_horizon_agent(stock_query)
    insider_agent = create_insider_trading_agent(stock_query)
    trends_agent = create_google_trends_agent(stock_query)
    dilution_agent = create_share_dilution_agent(stock_query)
    short_agent = create_short_interest_agent(stock_query)
    debt_agent = create_debt_analysis_agent(stock_query)
    infinite_agent = create_infinite_game_agent(stock_query)
    ceo_agent = create_ceo_analysis_agent(stock_query)
    analyst_agent = create_analyst_ratings_agent(stock_query)
    technical_agent = create_technical_analysis_agent(stock_query)
    reverse_agent = create_reverse_analysis_agent(stock_query)
    bond_agent = create_bond_correlation_agent(stock_query)
    
    aggregator = create_investment_aggregator()
    
    print(f"✅ Created {16} analysis agents")
    
    # Create parallel research team - all agents run simultaneously
    parallel_analysis_team = ParallelAgent(
        name="ParallelAnalysisTeam",
        sub_agents=[
            business_agent,
            competitive_agent,
            media_agent,
            ethics_agent,
            horizon_agent,
            insider_agent,
            trends_agent,
            dilution_agent,
            short_agent,
            debt_agent,
            infinite_agent,
            ceo_agent,
            analyst_agent,
            technical_agent,
            reverse_agent,
            bond_agent,
        ],
    )
    
    # Create sequential workflow: parallel analysis then aggregation
    root_agent = SequentialAgent(
        name="InvestmentAnalysisSystem",
        sub_agents=[parallel_analysis_team, aggregator],
    )
    
    print("✅ Investment analysis workflow created.")
    return root_agent
