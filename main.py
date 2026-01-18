# langchain_core is a highlevel framework that allows us to build AI applications.
# langgraph.prebuilt is a complex framework that allows us to build AI Agents
# langchain_openai is a module that allows us to interact with OpenAI's language models.
# dotenv is a module that allows us to load environment variables from a .env file.
from langchain_core.messages import HumanMessage 
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

@tool #glorified function
def calculator(a: float, b: float) -> str:
    """
    Docstring for calculator
    Useful for performing basic arithmetric calculations with numbers
    :param a: a number
    :type a: float
    :param b: a number
    :type b: float
    :return: a statements containing the results of an arithmetric calculation
    :rtype: str
    """
    print("Tool has been called!")
    return f"The sum of {a} and {b} is {a + b}"

def main():
    #Initialize the ChatOpenAI model with a temperature setting of 0
    # temperature controls the randomness of the model's output.
    # 0 means the model will produce more deterministic and focused responses.
    model = ChatOpenAI(temperature=0) 

    tools = [calculator] # a list to hold the tools the agent can use
    # Creates a prebuilt ReAct agent executor using the provided model and tools.
    agent_executor = create_react_agent(model, tools) 

    print("Welcome! I'm your AI Agent. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    # Chat loop
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == 'quit':
            break

        print("\nAssistant:", end="")
        # agent call
        # pass the user input to the agent executor.
        # the agent processes the input and generates a response as a stream of chunks.
        # chunks are incremental pieces of the response received from the agent.
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            # look through chunk for agents response. If the agent response has a message,
            # print the message response
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end=" ")
        print()

if __name__ == "__main__":
    main()
            
