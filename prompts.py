tavily_perplexity_search_subsidiaries_domain_prompt="""As an AI Search Engine,
    search all the web and provide correct URLs for information related to the
    company name provided as input.
    You are expected to provide correct URLs that contain information about
    the given company's subsidiaries and associated domains.
    Focus on reputable sources such as company websites,
    business directories, news articles,
    and other relevant online resources.
    Search the web for accurate and up-to-date information about the company provided in query. 
    Provide reliable URLs containing information on: 1. The company's subsidiaries 2. Associated domains and websites owned by the company.
    Focus on reputable sources such as: - Official company websites - Business directories (e.g., Bloomberg, Reuters) - Financial news websites - Industry-specific publications
    - Government databases (e.g., SEC filings for public companies). Prioritize recent and authoritative sources. Exclude unofficial blogs, personal websites,
    or unreliable sources.
    Provide a brief summary of what each URL contains, focusing on its relevance to the company's subsidiaries and associated domains."""
    

tavily_perplexity_search_query_prompt="""Search for and provide reliable web links\
    containing information about subsidiaries\
    and associated domains of the company: {company_name}.\
    Focus on authoritative sources such as official company websites,\
    business directories, and reputable news outlets.\
    For each link, briefly summarize its relevance to the company's\
    subsidiaries or associated domains."""


required_format_search_urls_response_prompt= """
You are an AI Content Extractor. Your job is to extract urls with the summary as text.
Return the information in the following list format:
[
    {
        "url": "https://www.test.com",
        "summary": "This is a summary of the content in the website"
    },
    {
        "url": "https://www.test1.com",
        "summary": "This is a summary of the content in the website"
    }
]
"""

web_crawl_url_prompt="""Extract the subsidiaries and associated domains of the company.Extracted model JSON format should look like this: 
                    {"subsidiaries":["subsidiaries1","subsidiaries2",...], "associated_domains": ["associated_domain_1","associated_domain_2",....]}."""
                    


response_generation_subsidiaries_domain_prompt="""You are an AI Agent. Your task is to extract the subsidiaries\
        and associated domains of the company.\
        Output format should be given json format:{"subsidiaries":["subsidiaries1","subsidiaries2",...], "associated_domains": ["associated_domain_1","associated_domain_2",...]}.
        Make sure keys are subsidiaries and associated_domains."""
        


