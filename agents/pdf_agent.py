"""PDF Agent"""
from typing import List

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
from togetherchain import TogetherLLM
from dotenv import load_dotenv

load_dotenv()
system_prompt_initial = """You are an expert interpreter of PDF documents. You are going to be presented with a PDF document and are expected to parse and make sense of its contents.

Upon invocation, follow these steps silently:

1. Read the PDF document carefully, processing it page by page.
2. Extract text from the PDF and read it line by line to make the best sense of it.
3. Understand each concept, detail, and piece of information within the document.
4. Extract any key lessons, takeaways, or important information from the document.

------------------PDF DOCUMENT--------------------------
{pdf_document}
-----------------END OF PDF DOCUMENT--------------------

Note: If any part of the document does not make sense or is unclear, please skip over it.

Take a deep breath, think step by step, analyze the document, and generate a lesson, summary, or any essential information from the given PDF document.

I will tip you $20 if you provide a perfect and accurate interpretation and summary, and I will fine you $40 if you miss any crucial information or introduce any changes or inaccuracies.
"""



prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),
    ]
)



# Choose the LLM that will drive the agent
llm = TogetherLLM(
    together_api_key=os.environ["TOGETHER_API_KEY"],
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0,
    max_tokens=12000
)



pdf_runnable = prompt | llm | StrOutputParser()
