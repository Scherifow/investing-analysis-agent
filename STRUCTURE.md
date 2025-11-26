# Investing Analysis Agent - Project Structure

This project has been refactored for better maintainability and separation of concerns.

## Project Structure

```
investing-analysis-agent/
├── agen.py          # Main entry point - orchestrates the workflow
├── config.py        # Configuration and environment setup
├── agents.py        # Individual agent definitions
├── workflow.py      # Workflow orchestration (Sequential/Parallel agents)
├── main.py          # Alternative entry point
├── pyproject.toml   # Project dependencies
├── .env             # Environment variables (not in git)
└── README.md        # This file
```

## Module Descriptions

### `config.py`
- Loads environment variables from `.env` file
- Validates `GOOGLE_API_KEY` presence
- Defines retry configuration for API calls
- Sets model configuration constants

### `agents.py`
- `create_tech_researcher()` - AI/ML trends research agent
- `create_health_researcher()` - Medical breakthroughs research agent
- `create_finance_researcher()` - Fintech trends research agent
- `create_aggregator_agent()` - Synthesizes all research into executive summary

### `workflow.py`
- `create_research_workflow()` - Orchestrates the complete workflow
- Creates parallel research team (runs 3 researchers simultaneously)
- Sets up sequential execution (parallel research → aggregation)

### `agen.py`
- Main entry point for running the research system
- Imports and executes the workflow
- Suitable for Jupyter notebook-style execution with `# %%` cell markers

## Usage

### Setup
1. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

### Running the Agent
```python
from google.adk.runners import InMemoryRunner
from workflow import create_research_workflow

# Create the workflow
root_agent = create_research_workflow()

# Run the research system
runner = InMemoryRunner(agent=root_agent)
response = await runner.run_debug(
    "Run the daily executive briefing on Tech, Health, and Finance"
)
```

## Benefits of This Structure

1. **Separation of Concerns**: Each module has a single, clear responsibility
2. **Reusability**: Agents can be imported and reused in different workflows
3. **Testability**: Individual components can be tested in isolation
4. **Maintainability**: Changes to one agent don't affect others
5. **Scalability**: Easy to add new agents or modify existing ones
6. **Configuration Management**: Centralized config makes it easy to adjust settings

## Adding New Agents

To add a new research agent:

1. Add a new function in `agents.py`:
   ```python
   def create_your_agent() -> Agent:
       """Your agent description."""
       return Agent(
           name="YourAgent",
           model=Gemini(model=MODEL_NAME, api_key=GOOGLE_API_KEY, retry_options=RETRY_CONFIG),
           instruction="Your instruction here",
           tools=[google_search],
           output_key="your_output_key",
       )
   ```

2. Import and add it to the workflow in `workflow.py`:
   ```python
   from agents import create_your_agent
   
   your_agent = create_your_agent()
   parallel_research_team = ParallelAgent(
       name="ParallelResearchTeam",
       sub_agents=[tech_researcher, health_researcher, finance_researcher, your_agent],
   )
   ```

3. Update the aggregator's instruction to include the new agent's output
