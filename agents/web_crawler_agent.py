from crawl4ai import WebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from models.pydantic_models import OpenAIModelInfoExtractor
from prompts import web_crawl_url_prompt
from config import settings


class WebCrawlerAgent:
    def __init__(self):
        self.crawler = WebCrawler()
        self.crawler.warmup()

    def crawl_urls(self, urls):
        consolidated_context = []
        for url in urls:
            result = self.crawler.run(
                url=url,
                word_count_threshold=1,
                extraction_strategy=LLMExtractionStrategy(
                    provider=settings.WEB_CRAWL_URL_PROVIDER,
                    api_token=settings.OPENAI_API_KEY,
                    schema=OpenAIModelInfoExtractor.schema(),
                    extraction_type="schema",
                    instruction=web_crawl_url_prompt,
                ),
                bypass_cache=True,
            )
            if result.extracted_content:
                consolidated_context.append(result.extracted_content)
        return ' '.join(str(item) for item in consolidated_context if item is not None)

