"""Configuration module for the research agent system."""
import os
from dotenv import load_dotenv
from google.genai import types

# Load environment variables
load_dotenv()

# Validate API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError(
        "🔑 Authentication Error: GOOGLE_API_KEY not found. "
        "Please add it to your .env file."
    )

# Retry configuration for API calls
RETRY_CONFIG = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

# Model configuration
MODEL_NAME = "gemini-2.5-flash-lite"

print("✅ Configuration loaded successfully.")
