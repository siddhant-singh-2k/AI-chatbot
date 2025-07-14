import  os


from dotenv import load_dotenv


load_dotenv()

# Setup LLM's & tools

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages.ai import AIMessage


openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model = "llama-3.3-70b-versatile")

search_tool = TavilySearchResults(max_results= 2)

# Setup agent with search functionality

from langgraph.prebuilt import  create_react_agent



def get_response_from_agent(llm_id,query,allowed_search,system_prompt,provider):

    if provider == "Groq":
        llm  = ChatGroq(model = llm_id)

    elif provider == "OpenAI":
        llm =  ChatOpenAI(model=llm_id)

    tools = [TavilySearchResults(max_results= 2)] if allowed_search == True else []
    agent = create_react_agent(
        model = llm,
        tools= tools,
        prompt = system_prompt
    )


    # query = "Tell me about the trends in crypto"

    state = {"messages":query}
    responses = agent.invoke(state)
    messages = responses.get("messages")

    ai_message = [message.content for message in messages if isinstance(message,AIMessage)]
    return ai_message[-1]



