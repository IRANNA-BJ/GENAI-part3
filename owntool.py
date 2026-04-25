from langchain.tools import tool

@tool
def get_greeting(name : str) ->str: #type hints
    """ generate a greeting message for a """
    
    return f"hello {name}, welcome to the AI  world"

result = get_greeting.invoke({"name":"akarsh"})
print(result)

print(get_greeting.name)
print(get_greeting.description)
print(get_greeting.args)