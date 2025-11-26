# 🔍 Investment Analysis Agent

An intelligent multi-agent system that conducts comprehensive investment analysis using Google's ADK (Agent Development Kit) and Gemini AI. This system orchestrates 16 specialized AI agents to analyze stocks from multiple perspectives and provide data-driven investment recommendations.

## 🌟 Features

- **Multi-Agent Architecture**: 16 specialized agents working in parallel for efficient analysis
- **Comprehensive Analysis**: Covers business fundamentals, technical indicators, sentiment analysis, and more
- **Google Search Integration**: Real-time data retrieval from across the web
- **Automated Report Generation**: Detailed markdown reports with BUY/HOLD/AVOID recommendations
- **Parallel Processing**: Agents run simultaneously for fast results
- **Configurable Retry Logic**: Robust error handling with automatic retries

## 📊 Analysis Dimensions

The system analyzes stocks across 16 key dimensions:

1. **Business Understanding** - Company's business model, products, and industry
2. **Competitive Advantage** - Unique moats and differentiators
3. **Media Sentiment** - Recent news coverage and public perception
4. **Ethics Check** - Corporate controversies and ethical concerns
5. **Investment Horizon** - Long-term (5+ years) hold potential
6. **Insider Trading** - Congressional and insider activity signals
7. **Google Trends** - Public interest and search trends
8. **Share Dilution** - Stock issuance and buyback programs
9. **Short Interest** - Market sentiment via short positions
10. **Debt Analysis** - Debt levels and financial health
11. **Infinite Game** - Long-term vs. short-term focus
12. **CEO Analysis** - Leadership quality and track record
13. **Analyst Ratings** - Professional analyst consensus
14. **Technical Analysis** - RSI and chart indicators
15. **Reverse Analysis** - Understanding price drops and catalysts
16. **Bond Correlation** - Interest rate sensitivity

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- Google API Key (for Gemini AI)

### Installation

#### Option 1: Using uv (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Scherifow/investing-analysis-agent.git
   cd investing-analysis-agent
   ```

2. **Install dependencies**
   ```bash
   uv sync
   source .venv/bin/activate
   ```

#### Option 2: Using pip

1. **Clone the repository**
   ```bash
   git clone https://github.com/Scherifow/investing-analysis-agent.git
   cd investing-analysis-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -e .
   ```

### Configuration

1. **Set up your Google API key**
   
   Create a `.env` file in the project root:
   ```bash
   GOOGLE_API_KEY=your_google_api_key_here
   ```
   
   Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## 💻 Usage

Run the investment analysis agent:

```bash
python main.py
```

The system will prompt you to enter a stock ticker or company name:

```
🔍 Investment Analysis Agent
==================================================

📊 Which stock or company would you like to analyze? MSFT

🚀 Analyzing MSFT...
==================================================
```

The agent will:
1. Create 16 specialized analysis agents
2. Execute parallel research across all dimensions
3. Aggregate findings into a comprehensive report
4. Save the analysis to the `analysis/` directory
5. Display results in the terminal

### Example Output

```
✅ Analysis complete!
==================================================

📋 Investment Analysis:
**Investment Recommendation: BUY**

Microsoft presents a compelling investment opportunity with robust competitive 
advantages, strong leadership, and strategic focus on AI and cloud computing...
```

Reports are saved as: `analysis/analysis_{TICKER}_{TIMESTAMP}.md`

## 🏗️ Architecture

### Agent Workflow

```
User Input (Stock Query)
    ↓
SequentialAgent (Root)
    ↓
ParallelAgent (16 Agents Running Simultaneously)
    ├── BusinessUnderstandingAgent
    ├── CompetitiveAdvantageAgent
    ├── MediaSentimentAgent
    ├── EthicsAgent
    ├── InvestmentHorizonAgent
    ├── InsiderTradingAgent
    ├── GoogleTrendsAgent
    ├── ShareDilutionAgent
    ├── ShortInterestAgent
    ├── DebtAnalysisAgent
    ├── InfiniteGameAgent
    ├── CEOAnalysisAgent
    ├── AnalystRatingsAgent
    ├── TechnicalAnalysisAgent
    ├── ReverseAnalysisAgent
    └── BondCorrelationAgent
    ↓
InvestmentAggregator
    ↓
Final Recommendation (BUY/HOLD/AVOID)
```

### Project Structure

```
investing-analysis-agent/
├── main.py              # Entry point and CLI interface
├── agents.py            # Agent definitions and creation functions
├── workflow.py          # Workflow orchestration (parallel + sequential)
├── config.py            # Configuration and environment variables
├── pyproject.toml       # Project dependencies
├── .env                 # API keys (not in repo)
├── analysis/            # Generated analysis reports
│   └── analysis_*.md    # Timestamped markdown reports
└── README.md            # This file
```

## ⚙️ Configuration

### Model Configuration

Edit `config.py` to customize:

```python
MODEL_NAME = "gemini-2.5-flash-lite"  # Gemini model to use

RETRY_CONFIG = types.HttpRetryOptions(
    attempts=5,           # Maximum retry attempts
    exp_base=7,          # Delay multiplier
    initial_delay=1,     # Initial delay in seconds
    http_status_codes=[429, 500, 503, 504]
)
```

### Agent Customization

Each agent in `agents.py` can be customized:
- Modify instructions for different analysis depth
- Adjust word count limits (currently 100-150 words per agent)
- Add or remove research dimensions

## 📝 Example Analysis Report

See the `analysis/` directory for sample reports. Each report includes:

- Investment recommendation (BUY/HOLD/AVOID)
- Detailed rationale with supporting evidence
- Key risks to consider
- Key opportunities for growth
- Analysis timestamp and duration

## 🛠️ Technologies Used

- **Google ADK (Agent Development Kit)**: Multi-agent orchestration
- **Google Gemini 2.5 Flash Lite**: LLM for analysis
- **Google Search**: Real-time data retrieval
- **Python 3.13+**: Core language
- **python-dotenv**: Environment variable management

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new analysis dimensions
- Improve agent instructions
- Enhance report formatting
- Add new data sources

## ⚠️ Disclaimer

**This tool is for educational and research purposes only.** The analysis provided is generated by AI agents and should not be considered as financial advice. Always conduct your own research and consult with qualified financial advisors before making investment decisions.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Scherifow**
- GitHub: [@Scherifow](https://github.com/Scherifow)

## 🙏 Acknowledgments

- Built with [Google's Agent Development Kit (ADK)](https://github.com/google/adk)
- Powered by [Google Gemini AI](https://deepmind.google/technologies/gemini/)

---

**Happy Investing! 📈**
