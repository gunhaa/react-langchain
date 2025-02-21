from dotenv import load_dotenv
from langchain.agents import tool

load_dotenv()

@tool
def get_text_length(text:str)-> int:
    # LLM이 이 도구를 추론 엔진에서 사용할지 말지 결정하기때문에
    # 문구가 매우 중요하다
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with {text=}")
    text=text.strip("'\n").strip((
        '"'
    )) # stripping away non alphabetic characters just in case

    return len(text)


if __name__ == "__main__":
    print("hello ReAct Langchain")
    tools = [get_text_length]

    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    
    Question: {input}
    Thought:
    """