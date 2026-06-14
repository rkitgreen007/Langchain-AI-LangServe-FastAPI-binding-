from langserve import RemoteRunnable
from langchain_core.messages import HumanMessage, AIMessage

# Point directly to your exposed LangServe endpoint
remote_chain = RemoteRunnable("http://localhost:8000/chat-rag/")

# Simulating historical multi-turn interaction state
history = [
    HumanMessage(content="What is the cluster scaling limit?"),
    AIMessage(content="Cluster scaling triggers automatically when CPU utilization hits 78%.")
]

# Use .stream() to fetch tokens asynchronously as they are produced by the LLM
chunks = remote_chain.stream({
    "input": "Does this trigger change if the memory limit changes?",
    "chat_history": history
})

print("AI Response: ", end="")
for chunk in chunks:
    print(chunk, end="", flush=True)
print()
