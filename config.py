import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")
    PERPLEXITY_API_KEY: str = os.getenv("PERPLEXITY_API_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    WEB_CRAWL_URL_PROVIDER= os.getenv("WEB_CRAWL_URL_PROVIDER")
    OPENAI_MODEL= os.getenv("OPENAI_MODEL")

settings = Settings()