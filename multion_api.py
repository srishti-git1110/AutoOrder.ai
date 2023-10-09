from config import config

import multion
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits.multion.toolkit import MultionToolkit

def get_multion_output(instruction):
    multion.login()
    llm = OpenAI(
        temperature=0, 
        openai_api_key=config.openai_api_key
    )

    toolkit = MultionToolkit()
    tools=toolkit.get_tools()

    agent = initialize_agent(
        tools=toolkit.get_tools(),
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    output = agent.run()

    return output
