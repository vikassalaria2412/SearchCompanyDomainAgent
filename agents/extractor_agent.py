from langchain_openai import ChatOpenAI
from config import settings
import json
from prompts import response_generation_subsidiaries_domain_prompt

class ExtractorAgent:
    def __init__(self):
        self.model_id = settings.OPENAI_MODEL
        self.llm = ChatOpenAI(model=self.model_id, temperature=0, max_tokens=4000)

    def extract_subsidiaries_and_domains(self, context):
        prompt = response_generation_subsidiaries_domain_prompt
        
        messages = [
            ("system", prompt),
            ("human", context),
        ]
        
        response = self.llm.invoke(messages)
        response_content = response.content
        
        # Clean up the response if it contains JSON markers
        if response_content.startswith("```json"):
            response_content = response_content.replace('```json\n', '').replace('\n```', '')
        
        return json.loads(response_content)