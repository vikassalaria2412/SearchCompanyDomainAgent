from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from config import settings
from prompts import tavily_perplexity_search_subsidiaries_domain_prompt,\
    tavily_perplexity_search_query_prompt,required_format_search_urls_response_prompt
import json


class SearchAgent:
    def __init__(self):
        self.tavily_search = TavilySearchResults(
            TAVILY_API_KEY=settings.TAVILY_API_KEY,
            description=tavily_perplexity_search_subsidiaries_domain_prompt,
            max_results=10,
            include_answer=True,
            include_images=True
        )
        self.perplexity_chat = ChatPerplexity(
            temperature=0,
            pplx_api_key=settings.PERPLEXITY_API_KEY,
            model="llama-3-sonar-small-32k-online"
        )

    def tavily_search_results(self, company_name: str):
        query = tavily_perplexity_search_query_prompt.format(company_name=company_name)
        results = self.tavily_search.invoke({"query": query})
        return [result['url'] for result in results]

    def perplexity_search_results(self, company_name: str):
        system_prompt = tavily_perplexity_search_subsidiaries_domain_prompt
        human_prompt = tavily_perplexity_search_query_prompt.format(company_name=company_name)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", human_prompt)
        ])
        
        chain = prompt | self.perplexity_chat | StrOutputParser()
        response = chain.invoke({"input": human_prompt})
        perplexity_web_result=self.custom_response_perplexity_search_results(response)
        perplexity_web_result = json.loads(perplexity_web_result)
        perplexity_search_urls = [result['url'] for result in perplexity_web_result]
        return perplexity_search_urls

    
    def custom_response_perplexity_search_results(self, response):
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "{system}"),
                ("human", "Response is :{response}"),
                ]
            )
        llm = obj_openai.gpt_model_call()
        chain = prompt | llm | StrOutputParser()
        
        perplexity_response = chain.invoke(
            {
                "system": required_format_search_urls_response_prompt,
                "response": response
                }
            )
        return perplexity_response
    
    def combine_search_results(self, tavily_results, perplexity_results):
        return list(set(tavily_results) | set(perplexity_results))
    
    
    
    
    
    
    
class OpenAIResponse:
    def __init__(self):
        self.openai_model = "gpt-4o"
    
    
    def gpt_model_call(self):
        llm = ChatOpenAI(model=self.openai_model, temperature=0,max_tokens=4000)
        return llm
    
    
obj_openai = OpenAIResponse()