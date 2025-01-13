# sandbox-llamaindex

A sandbox to play with LlamaIndex

## Environment Setup

1. Clone this repository
2. Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_openai_api_key_here
LLAMA_INDEX_CACHE_DIR=./cache
LLAMA_INDEX_EMBEDDING_MODEL=text-embedding-ada-002
VECTOR_STORE_TYPE=simple
VECTOR_STORE_PATH=./vector_store
LLAMA_INDEX_LOG_LEVEL=INFO
```
3. Replace `your_openai_api_key_here` with your actual OpenAI API key
4. Make sure the `.env` file is added to `.gitignore`

## Project Structure

- `cache/`: LlamaIndex cache directory
- `vector_store/`: Vector store for embeddings
- `.env`: Environment configuration

## Requirements

- Python 3.8+
- OpenAI API key
