"""Main entry point for the investing analysis agent."""
import asyncio
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
    
    # Create the research workflow
    root_agent = create_research_workflow()
    
    # Run the analysis
    runner = InMemoryRunner(agent=root_agent)
    response = await runner.run_debug(
        f"Analyze the investment potential of {stock_query}. "
        f"Research recent technology trends, health innovations, and financial developments "
        f"related to {stock_query}. Provide a comprehensive executive summary."
    )
    
    print("\n" + "=" * 50)
    print("✅ Analysis complete!")
    print("=" * 50)
    
    # Display the results
    if hasattr(response, 'session_state') and 'executive_summary' in response.session_state:
        print("\n📋 Executive Summary:")
        print(response.session_state['executive_summary'])
    else:
        print("\n📋 Response:")
        print(response)


if __name__ == "__main__":
    asyncio.run(main())
