from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_community import 

information = """
    Elon Reeve Musk FRS (/ˈiːlɒn/; born June 28, 1971) is a businessman and investor, known for his key roles in the space company SpaceX and the automotive company Tesla, Inc. Other involvements include ownership of X Corp., the company that operates the social media platform X (formerly known as Twitter), and his role in the founding of The Boring Company, xAI, Neuralink, and OpenAI. He is one of the wealthiest individuals in the world; as of August 2024 Forbes estimates his net worth to be US$247 billion.
"""

if __name__ == "__main__":
    print ("Hello LangChain")
    
    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them 
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template )
    
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key = "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" )
    llm = ChatOllama(model="llama3.1")
    
    chain = summary_prompt_template | llm
    
    res = chain.invoke(input={"information": information})
    
    print(res)