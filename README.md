# RAG
Rag (Retreival Augmented Generation) Python solution with llama3, LangChain, Ollama and ChromaDB in a Flask API based solution

# About
In this project we have used llama3 model and using Flask ai to access ML model with query.
Please download Ollama3 from `https://ollama.com/`
There are 3 apis
- POST /ai where we need to provide json body with parameter `query` example: {"query": "Tell me a goat joke"}.
- POST /pdf where you provide pdf file, body is form-data key as `file` and value `input_file`.
- POST /ask_pdf here you get the info about the uploaded pdf file need to provide json body with parameter `query` example: {"query": "who is Alice?"}.

# How to run Application in local

- Ollama must be running in your local. you can check if `http://localhost:11434/` gives `Ollama is running`
- Install pip libraries `pip install -r requirements.txt`
- Run `python app.py`

# ScreenShot

<div>
    <img src="https://github.com/RickyRiko305/Llama3-PDF-RAG-API/blob/main/pic/llama_flask_1.PNG">
    <br>
    <img src="https://github.com/RickyRiko305/Llama3-PDF-RAG-API/blob/main/pic/llama_flask_2.PNG">
    <br>
    <img src="https://github.com/RickyRiko305/Llama3-PDF-RAG-API/blob/main/pic/llama_flask_3.PNG">
</div>