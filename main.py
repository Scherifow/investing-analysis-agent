"""Main entry point for the investing analysis agent."""
import asyncio
import os
from datetime import datetime
from google.adk.runners import InMemoryRunner
from workflow import create_research_workflow


async def main():
    """Run the investing analysis agent with user input."""
    print("🔍 Investment Analysis Agent")
    print("=" * 50)
    
    # Prompt user for stock/company to analyze
    stock_query = input("\n📊 Which stock or company would you like to analyze? ")
    
    if not stock_query.strip():
        print("❌ No stock provided. Exiting...")
        return
    
    print(f"\n🚀 Analyzing {stock_query}...")
    print("=" * 50)
    
    # Create the research workflow with the stock query
    root_agent = create_research_workflow(stock_query)
    
    # Run the analysis
    runner = InMemoryRunner(agent=root_agent)
    await runner.run_debug(
        f"Conduct a comprehensive investment analysis of {stock_query}. "
        f"Provide factual, unbiased information across all research areas. "
        f"Focus on delivering pure data and objective insights without speculation or bias.",
        quiet=True
    )
    
    print("\n" + "=" * 50)
    print("✅ Analysis complete!")
    print("=" * 50)
    
    # Get the session to access the state
    session = await runner.session_service.get_session(
        app_name=runner.app_name,
        session_id="debug_session_id",
        user_id="debug_user_id"
    )

    if session and session.state:
        # Create analysis directory if it doesn't exist
        os.makedirs("analysis", exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"analysis/analysis_{stock_query}_{timestamp}.md"
        
        markdown_content = f"# Investment Analysis: {stock_query}\n\n"
        markdown_content += f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # Add recommendation first if available
        if 'investment_recommendation' in session.state:
            markdown_content += "## 📋 Investment Recommendation\n\n"
            markdown_content += f"{session.state['investment_recommendation']}\n\n"
            markdown_content += "---\n\n"
            
        markdown_content += "## 🔍 Detailed Research Data\n\n"
        
        # List of all agent output keys
        analysis_keys = [
            ("Business Understanding", "business_understanding"),
            ("Competitive Advantage", "competitive_advantage"),
            ("Media Sentiment", "media_sentiment"),
            ("Ethics Check", "ethics_check"),
            ("Investment Horizon", "investment_horizon"),
            ("Insider Trading", "insider_trading"),
            ("Google Trends", "google_trends"),
            ("Share Dilution", "share_dilution"),
            ("Short Interest", "short_interest"),
            ("Debt Analysis", "debt_analysis"),
            ("Infinite Game", "infinite_game"),
            ("CEO Analysis", "ceo_analysis"),
            ("Analyst Ratings", "analyst_ratings"),
            ("Technical Analysis", "technical_analysis"),
            ("Reverse Analysis", "reverse_analysis"),
            ("Bond Correlation", "bond_correlation"),
        ]
        
        for title, key in analysis_keys:
            if key in session.state:
                markdown_content += f"### {title}\n\n"
                markdown_content += f"{session.state[key]}\n\n"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        print(f"\n💾 Analysis saved to: {filename}")
    
    # Display the results
    if session and session.state and 'investment_recommendation' in session.state:
        print("\n📋 Investment Analysis:")
        print(session.state['investment_recommendation'])
    else:
        print("\n📋 Response:")
        print("No recommendation found in session state.")


if __name__ == "__main__":
    asyncio.run(main())
