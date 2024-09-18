import os
import requests
from dotenv import load_dotenv

class User:
    def __init__ (self, id, username, balance, debt):
        self.id = id
        self.username = username
        self.balance = balance
        self.debt = debt

test_data = [
    User(1, 'minh13', 4000, debt=9090),
    User(id=2, username='loc14', balance=5000, debt=49320)   
]

def query_info(username, query_attributes: list ) -> str:
    balance = 0
    output=[]
    for user in test_data:
        if user.username == username:
            for attribute in query_attributes:
                if attribute in user:
                    output.append(100)
            output_str = ''.join(output) 
            return output_str
    return output
    