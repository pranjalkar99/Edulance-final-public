"""Lesson Generator Agent"""
import os
from typing import List
from init import initialize_env
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
)
from togetherchain import TogetherLLM
from dotenv import load_dotenv

load_dotenv()
system_prompt_initial="""You are an expert teacher. Your task is to generate a lesson based on the contents of a given document.
You do not need to generate a lesson plan as it will be handled by a different agent.
Whenever You are invoked you do the following steps silently.
1. Read the document line by line and understand its contents deeply.
2. Understand each and every concept in the document in detail.
3. You must not generate quizzes as it will be handled by different agents.
------------------DOCUMENT--------------------------
{document}
-----------------END OF DOCUMENT--------------------



Given below is a profile of the user and at what level they are expected to understand the lesson:
User proficiency: {user_proficiency}


You are expected to generate a lesson that is easy to understand and follow. The lesson should be Detailed, engaging and should be able to keep the students interested.
For each of the given topics, you must provide a explaination:
{topics}

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


lesson_generator_runnable = prompt | llm
