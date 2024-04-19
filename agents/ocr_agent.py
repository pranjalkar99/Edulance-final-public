"""Lesson Generator Agent"""
import os
from typing import List
from init import initialize_env
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_together import Together
from langchain_core.output_parsers import StrOutputParser
from togetherchain import TogetherLLM
from dotenv import load_dotenv

load_dotenv()
system_prompt_initial="""You are an expert interpreter. You are going to get ocr results from a document and you are expected to parse it properly and make sense of it.
If it doesnt make any sense, you may skip the part which doesnt make any sense.

Whenever You are invoked you do the following steps silently.
1. Read the document line by line and try to make the best sense out of it.
2. Understand each and every concept in the document in detail.

------------------DOCUMENT--------------------------
{document}
-----------------END OF DOCUMENT--------------------


I will tip you $20 if you are perfect, and I will fine you $40 if you miss any important information or change hallucinate up details.

Take a deep breath, think step by step, analyze the document and generate a lesson:
"""


prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt_initial),
    ]
)

initialize_env()
llm = TogetherLLM(
    together_api_key=os.environ["TOGETHER_API_KEY"],
    model="meta-llama/Llama-3-8b-chat-hf",
    temperature=0,
    max_tokens=3500
)

ocr_runnable = prompt | llm | StrOutputParser()
