<div align="center">
  <img src="logo.png" alt="sandbox-llamaindex" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
  [![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG-purple.svg)](https://www.llamaindex.ai/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **A sandbox for experimenting with LlamaIndex RAG (Retrieval-Augmented Generation) pipelines**

  [LlamaIndex Docs](https://docs.llamaindex.ai/) · [OpenAI API](https://platform.openai.com/)
</div>

## Overview

This project demonstrates a basic RAG pipeline using LlamaIndex. It loads documents, creates vector embeddings, and enables semantic querying over your data using OpenAI's models.

## Features

- **Document Loading**: Ingest documents from local directories
- **Vector Indexing**: Create searchable embeddings using OpenAI
- **Semantic Search**: Query your documents with natural language

## Quick Start

```bash
# Clone and set up environment
git clone https://github.com/tsilva/sandbox-llamaindex.git
cd sandbox-llamaindex
conda env create -f environment.yml
conda activate sandbox-llamaindex

# Configure API key
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run
python main.py
```

## Installation

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [OpenAI API Key](https://platform.openai.com/api-keys)

### Environment Setup

1. Create the conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate sandbox-llamaindex
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   ```

3. Add your OpenAI API key to `.env`:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Add your documents to the `data/` directory, then run:

```bash
python main.py
```

The script will:
1. Load all documents from `data/`
2. Create vector embeddings using OpenAI
3. Build a searchable index
4. Run a sample query and print the response

### Example

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load documents
documents = SimpleDirectoryReader("./data").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine()
response = query_engine.query("What is this document about?")
print(response)
```

## Project Structure

```
sandbox-llamaindex/
├── main.py              # Entry point with RAG pipeline
├── data/                # Source documents directory
├── environment.yml      # Conda environment specification
├── .env.example         # Environment variables template
└── CLAUDE.md            # Claude Code instructions
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `llama-index-core` | Core LlamaIndex framework |
| `llama-index-llms-openai` | OpenAI LLM integration |
| `llama-index-embeddings-openai` | OpenAI embeddings |
| `llama-index-readers-file` | File reading utilities |
| `python-dotenv` | Environment variable management |

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is open source and available under the MIT License.
