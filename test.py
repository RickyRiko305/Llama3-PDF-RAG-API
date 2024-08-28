from langchain_community.llms import Ollama


llm = Ollama(model="llama3")

response = llm.invoke("Tell me a cow joke")

print(response)