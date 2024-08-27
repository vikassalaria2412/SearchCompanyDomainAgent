from fastapi import APIRouter, HTTPException
from models.pydantic_models import CompanySearchRequest, CompanySearchResponse
from agents.search_agent import SearchAgent
from agents.web_crawler_agent import WebCrawlerAgent
from agents.extractor_agent import ExtractorAgent

router = APIRouter()

@router.post("/search_company", response_model=CompanySearchResponse)
async def search_company(request: CompanySearchRequest):
    search_service = SearchAgent()
    web_crawler_service = WebCrawlerAgent()
    openai_service = ExtractorAgent()

    # Perform searches
    tavily_results = search_service.tavily_search_results(request.company_name)
    perplexity_results = search_service.perplexity_search_results(request.company_name)
    combined_urls = search_service.combine_search_results(tavily_results, perplexity_results)

    # Crawl URLs
    crawled_context = web_crawler_service.crawl_urls(combined_urls)

    # Extract information using OpenAI
    extracted_info = openai_service.extract_subsidiaries_and_domains(crawled_context)

    return CompanySearchResponse(
        company_name=request.company_name,
        results=extracted_info
    )