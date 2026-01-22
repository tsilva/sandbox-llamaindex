# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a sandbox environment for experimenting with LlamaIndex, a data framework for LLM applications. The project demonstrates basic RAG (Retrieval-Augmented Generation) using document indexing and querying.

## Environment Setup

The project uses conda for Python environment management. Set up the environment:

```bash
conda env create -f environment.yml
conda activate sandbox-llamaindex
```

Configure environment variables by creating `.env` from `.env.example`:
```bash
cp .env.example .env
```

Required environment variable:
- `OPENAI_API_KEY`: Your OpenAI API key for embeddings and LLM queries

Optional environment variables (referenced in README but not currently used in code):
- `LLAMA_INDEX_CACHE_DIR`: Cache directory path
- `LLAMA_INDEX_EMBEDDING_MODEL`: Embedding model name
- `VECTOR_STORE_TYPE`: Vector store type
- `VECTOR_STORE_PATH`: Vector store path
- `LLAMA_INDEX_LOG_LEVEL`: Logging level

## Running the Code

Execute the main script:
```bash
python main.py
```

The script:
1. Loads documents from the `data/` directory using `SimpleDirectoryReader`
2. Creates a vector index using `VectorStoreIndex`
3. Queries the index with a sample question about the documents
4. Prints the response

## Architecture

**Data Flow:**
1. Documents in `data/` are loaded by LlamaIndex's `SimpleDirectoryReader`
2. Documents are embedded and indexed using `VectorStoreIndex` (uses OpenAI embeddings by default)
3. Queries go through the query engine which retrieves relevant chunks and generates answers

**Key Components:**
- `main.py`: Entry point with basic RAG pipeline
- `data/`: Contains source documents (currently Frankenstein from Project Gutenberg)
- `environment.yml`: Conda environment specification with LlamaIndex dependencies

**LlamaIndex Stack:**
- `llama-index-core`: Core framework
- `llama-index-llms-openai`: OpenAI LLM integration
- `llama-index-readers-file`: File reading utilities
- `llama-index-embeddings-openai`: OpenAI embedding models

## Important Notes

- The project currently uses a simple in-memory vector store (default behavior)
- Environment variables for cache and vector store paths are documented but not implemented
- README.md must be kept up to date with any significant project changes
