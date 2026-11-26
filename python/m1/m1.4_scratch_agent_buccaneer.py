from deepagents import create_deep_agent

from models import model

system_prompt = """You are a portly, but hearty sailor who wants nothing more but to be out at sea with his crew.
You often make analogies using your experiences at sea, which include terrible storms, encounters with pirates,
and an unforgettable mutiny that you survived. Answer questions with enthusiasm and grit. Do not break character
under any circumstances.
"""

agent = create_deep_agent(
    model=model,
    system_prompt=system_prompt,
    name="buccaneer_agent",
)

result = agent.invoke({"messages": [{"role": "user", "content": "What is an LLM?"}]})

print(result["messages"][-1].text)