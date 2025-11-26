"""Investment analysis agents for comprehensive stock research."""
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from config import GOOGLE_API_KEY, RETRY_CONFIG, MODEL_NAME


def create_business_understanding_agent(stock_query: str) -> Agent:
    """Agent to understand what the company does and its industry."""
    agent = Agent(
        name="BusinessUnderstandingAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research and explain what {stock_query} does and its industry. 
        Answer: Do you understand their business model? What products/services do they offer? 
        What industry are they in? Keep concise (150 words).""",
        tools=[google_search],
        output_key="business_understanding",
    )
    return agent


def create_competitive_advantage_agent(stock_query: str) -> Agent:
    """Agent to identify unique competitive advantages."""
    agent = Agent(
        name="CompetitiveAdvantageAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research {stock_query}'s unique competitive advantages. 
        What makes them different from competitors? What is their moat? 
        Do they have patents, brand power, network effects, or cost advantages? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="competitive_advantage",
    )
    return agent


def create_media_sentiment_agent(stock_query: str) -> Agent:
    """Agent to analyze media coverage and sentiment."""
    agent = Agent(
        name="MediaSentimentAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Search for recent news headlines about {stock_query}. 
        Analyze the sentiment: Is the media coverage positive, negative, or mixed? 
        What are the main topics in the news? Any controversies or achievements? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="media_sentiment",
    )
    return agent


def create_ethics_agent(stock_query: str) -> Agent:
    """Agent to check ethical concerns and controversies."""
    agent = Agent(
        name="EthicsAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research if {stock_query} has any ethical concerns, controversies, 
        or scandals. Check for labor practices, environmental issues, legal problems, 
        or unethical behavior. Is this a company with good values? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="ethics_check",
    )
    return agent


def create_investment_horizon_agent(stock_query: str) -> Agent:
    """Agent to evaluate long-term hold potential."""
    agent = Agent(
        name="InvestmentHorizonAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research if {stock_query} is suitable for long-term investment (5+ years). 
        Check their long-term strategy, market trends, growth potential, and sustainability. 
        Would you want to hold this stock for more than 5 years? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="investment_horizon",
    )
    return agent


def create_insider_trading_agent(stock_query: str) -> Agent:
    """Agent to check congressional and insider trading."""
    agent = Agent(
        name="InsiderTradingAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Search for information about congressional trading and insider activity 
        for {stock_query}. Check sites like housestockwatcher.com or quiverquant.com. 
        Are congresspeople or insiders buying or selling? What does this signal? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="insider_trading",
    )
    return agent


def create_google_trends_agent(stock_query: str) -> Agent:
    """Agent to analyze Google Trends data."""
    agent = Agent(
        name="GoogleTrendsAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research Google Trends data for {stock_query}. 
        Is interest in the company/brand growing or declining? 
        What does search trend data tell us about public interest? 
        Keep concise (100 words).""",
        tools=[google_search],
        output_key="google_trends",
    )
    return agent


def create_share_dilution_agent(stock_query: str) -> Agent:
    """Agent to check share dilution and new stock issuance."""
    agent = Agent(
        name="ShareDilutionAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research how many new shares {stock_query} is issuing. 
        Check for stock dilution, share buybacks, or new offerings. 
        Is the share count increasing (bad for investors) or decreasing (good)? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="share_dilution",
    )
    return agent


def create_short_interest_agent(stock_query: str) -> Agent:
    """Agent to check short interest ratio."""
    agent = Agent(
        name="ShortInterestAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research the short interest for {stock_query}. 
        What percentage of shares are being shorted? Is this high or low? 
        What does this indicate about market sentiment? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="short_interest",
    )
    return agent


def create_debt_analysis_agent(stock_query: str) -> Agent:
    """Agent to analyze company debt levels."""
    agent = Agent(
        name="DebtAnalysisAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research {stock_query}'s debt levels. 
        How much debt do they have? What is their debt-to-equity ratio? 
        How long would it take them to pay off their debt with current earnings? 
        Is the debt manageable or concerning? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="debt_analysis",
    )
    return agent


def create_infinite_game_agent(stock_query: str) -> Agent:
    """Agent to check if company plays the infinite game (long-term thinking)."""
    agent = Agent(
        name="InfiniteGameAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research if {stock_query} is focused on long-term success vs short-term profits. 
        Do they reinvest in R&D, employees, and innovation? 
        Are they building for the future or maximizing quarterly earnings? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="infinite_game",
    )
    return agent


def create_ceo_analysis_agent(stock_query: str) -> Agent:
    """Agent to analyze the CEO and leadership."""
    agent = Agent(
        name="CEOAnalysisAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research {stock_query}'s CEO and leadership team. 
        Who is the CEO? What is their background and track record? 
        Are they focused on long-term value creation or short-term gains? 
        Do they have skin in the game (own significant shares)? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="ceo_analysis",
    )
    return agent


def create_analyst_ratings_agent(stock_query: str) -> Agent:
    """Agent to check analyst ratings from Danelfin, TipRanks, GuruFocus."""
    agent = Agent(
        name="AnalystRatingsAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Search for analyst ratings and scores from Danelfin, TipRanks, 
        and GuruFocus for {stock_query}. What are the consensus ratings? 
        What do professional analysts think about this company? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="analyst_ratings",
    )
    return agent


def create_technical_analysis_agent(stock_query: str) -> Agent:
    """Agent to check RSI and technical indicators."""
    agent = Agent(
        name="TechnicalAnalysisAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research technical indicators for {stock_query}, especially RSI 
        (Relative Strength Index). Is the stock overbought or oversold? 
        What do the technical charts suggest? 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="technical_analysis",
    )
    return agent


def create_reverse_analysis_agent(stock_query: str) -> Agent:
    """Agent to understand why the stock dropped and reverse analysis."""
    agent = Agent(
        name="ReverseAnalysisAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""If {stock_query} has dropped recently, research WHY. 
        What caused the decline? Is it temporary or fundamental? 
        Do your homework on recent price movements and catalysts. 
        Keep concise (150 words).""",
        tools=[google_search],
        output_key="reverse_analysis",
    )
    return agent


def create_bond_correlation_agent(stock_query: str) -> Agent:
    """Agent to check 10-year US bond influence on stock."""
    agent = Agent(
        name="BondCorrelationAgent",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction=f"""Research how the 10-year US Treasury bond yields affect {stock_query}. 
        Is this company sensitive to interest rate changes? 
        How does rising/falling bond yields impact the stock price? 
        Keep concise (100 words).""",
        tools=[google_search],
        output_key="bond_correlation",
    )
    return agent


def create_investment_aggregator() -> Agent:
    """Aggregator to synthesize all investment research into final recommendation."""
    agent = Agent(
        name="InvestmentAggregator",
        model=Gemini(
            model=MODEL_NAME,
            api_key=GOOGLE_API_KEY,
            retry_options=RETRY_CONFIG
        ),
        instruction="""Synthesize all the research findings into a comprehensive investment analysis:

**Business Understanding:**
{business_understanding}

**Competitive Advantage:**
{competitive_advantage}

**Media Sentiment:**
{media_sentiment}

**Ethics Check:**
{ethics_check}

**Investment Horizon:**
{investment_horizon}

**Insider Trading:**
{insider_trading}

**Google Trends:**
{google_trends}

**Share Dilution:**
{share_dilution}

**Short Interest:**
{short_interest}

**Debt Analysis:**
{debt_analysis}

**Infinite Game:**
{infinite_game}

**CEO Analysis:**
{ceo_analysis}

**Analyst Ratings:**
{analyst_ratings}

**Technical Analysis:**
{technical_analysis}

**Reverse Analysis:**
{reverse_analysis}

**Bond Correlation:**
{bond_correlation}

Provide a clear investment recommendation: BUY, HOLD, or AVOID. 
Explain the key reasons for your recommendation.
Highlight the main risks and opportunities.
Summary should be around 400-500 words.""",
        output_key="investment_recommendation",
    )
    return agent
