import os
from typing import Optional
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
class User:
    def __init__(self, id, username, balance, debt):
        self.id = id
        self.username = username
        self.balance = balance
        self.debt = debt
    def __str__(self):
        return f'id={self.id},username={self.username},balance={self.balance},debt={self.debt}'

fake_data = [
    User(id=1, username='loctran', balance=200, debt=0),
    User(id=2, username='minhnguyen', balance=200, debt=2000000),
]

def query_information(username: str) -> User:
    for user in fake_data:
        if username in user.username:
            return user
    return None

def get_information_from_object(object: User) -> str:
    return repr(object)

def lookup(username: str, requested_information: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo"
    )

    template = """
        Given the account {username}, I want you to give me only the information requested {requested_information} 
        in the form of a string. Your answer should only contain the requested bank account information.
    """

    prompt_template = PromptTemplate(
        input_variables=["username", "requested_information"], 
        template=template
    )

    tools_for_agent = [
        Tool(
            name="Query database for bank account information",
            func=get_information_from_object,
            description="Retrieve specific attributes of the object in the form of string"
        ),
        Tool(
            name="Convert Object to String",
            func=query_information,
            description="Retrieve specific bank account information for a user, only give the username itself in the param"
        ),
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(username=username, requested_information=requested_information)}
    )

    account_information = result["output"]
    
    return account_information


if __name__ == "__main__":
    load_dotenv()
    # Pass the requested information as a comma-separated string
    output = lookup(username="minhnguyen", requested_information="balance,debt,id")
    print(output)
# class User:
#     def __init__ (self, id, username, balance, debt):
#         self.id = id
#         self.username = username
#         self.balance = balance
#         self.debt = debt
        
#     def __str__(self):
#         return f'id: {self.id},username:{self.username},balance:{self.balance},debt:{self.debt}'

# test_data = [
#     User(1, 'minh13', 4000, debt=9090),
#     User(id=2, username='loc14', balance=5000, debt=49320)   
# ]

# def query_info(username: str) -> User:

#     for user in test_data:
#         if user.username == username:
#             return user
#     return None
    
# def object_to_string(user_obj: User) -> str:

#     return repr(user_obj)
    


# def lookup(username: str, requested_info:str) -> str:
#     llm = ChatOpenAI(
#         temperature=0,
#         model_name = "gpt-3.5-turbo"
#     )
    
#     template = """
#         given the username {username}, return the information {requested_info} associated with that username
#         Your answer should only contain the requested information
#     """
    
#     prompt_template = PromptTemplate(
#         input_variables=["username", "requested_info"],
#         template=template
#     )
    
#     tools_for_agent = [
#         Tool(
#             name = "Query database for account info",
#             func = query_info,
#             description="Get information on bank account. Need to pass in only 1 argument, username. It will return an object"
#         ),
#         Tool(
#             name = "Parse object to string",
#             func = object_to_string,
#             description="Useful when converting object to string, which means showing attributes of an object"
#         )
#     ]
    
#     react_prompt = hub.pull("hwchase17/react")
#     agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
#     agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
#     result = agent_executor.invoke(
#         input = {"input": prompt_template.format_prompt(username=username, requested_info=requested_info)}
        
#     )
    
#     account_info = result["output"]
    
    
#     return account_info

# if __name__ == "__main__":
#     output = lookup("minh13", "balance, debt")
#     print(output)