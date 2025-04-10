import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from prompts import dialectic_prompt2
from dotenv import load_dotenv

load_dotenv()

def create_tutor_chain():
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")

    # Specify the input key used for memory context tracking
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        input_key="student_input",  
        return_messages=True
    )

    chain = LLMChain(
        llm=llm,
        prompt=dialectic_prompt2,
        memory=memory,
        verbose=True
    )
    return chain
