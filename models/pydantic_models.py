from pydantic import BaseModel, Field
from typing import List

class CompanySearchRequest(BaseModel):
    company_name: str

class SubsidiariesAssociatedDomains(BaseModel):
    subsidiaries: List[str]
    associated_domains: List[str]

class CompanySearchResponse(BaseModel):
    company_name: str
    results: SubsidiariesAssociatedDomains

class OpenAIModelInfoExtractor(BaseModel):
    model_name: str = Field(..., description="Subsidiaries and Associated Domains Extractor")
    input_data: str = Field(..., description="Extract subsidiaries and associated domains of the company.")
    output_data: str = Field(..., description="Output as Extracted subsidiaries and associated domains of the company.")