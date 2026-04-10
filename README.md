# AI-Powered RAG Business Report Analyst

A Retrieval-Augmented Generation (RAG) application that enables business analysts to extract key insights from lengthy reports through natural-language queries — built as a capstone project for the **UT Austin Postgraduate Program in AI / ML (Agentic AI specialization)**.

## Problem Statement

Business analysts at firms like Andreessen Horowitz are inundated with dense reports, research papers, and documents critical to strategic decision-making. Manually reading through a report like Harvard Business Review's "How Apple is Organized for Innovation" is time-consuming and inefficient.

By combining Semantic Search with Retrieval-Augmented Generation, analysts can directly ask questions like "How does Apple structure its teams for innovation?" and receive immediate, grounded answers drawn from the actual document — with source citations.

## Solution

A RAG pipeline that:

- Answers user queries by retrieving relevant content directly from lengthy documents
- Supports natural-language interaction without requiring a full manual read-through
- Cites sources and gracefully handles out-of-scope questions
- Compares three approaches: raw LLM, prompt-engineered LLM, and full RAG

## RAG Pipeline Architecture

| Stage | Implementation |
|-------|---------------|
| Document Loading | PyMuPDF (11-page PDF → page objects) |
| Chunking | RecursiveCharacterTextSplitter (256 tokens, 20 overlap, `cl100k_base` tokenizer) |
| Embedding | OpenAI Embeddings |
| Vector Store | ChromaDB |
| Retrieval | Chroma similarity search (top-k) + BM25 hybrid retrieval infrastructure |
| Generation | GPT-4o-mini with system prompt + retrieved context |
| Evaluation | GPT-4o scoring on groundedness and precision |

### Retrieval Strategy

- Primary: Chroma vector similarity search (k=3, or k=6 for metadata-heavy queries)
- First-chunk injection: Title page always included to ensure author/publisher metadata is available
- Hybrid infrastructure: BM25Retriever + EnsembleRetriever imports for keyword + semantic search

## Three Response Modes

The notebook implements and compares three approaches to demonstrate the value of RAG:

1. **Raw LLM** — No context, no system prompt (baseline)
2. **Prompt-Engineered LLM** — System prompt but no retrieved context
3. **Full RAG** — System prompt + retrieved document context (grounded)

## Results

### Evaluation Metrics

Responses are scored by GPT-4o on two dimensions (0.0–1.0 scale):

- **Groundedness**: How well the response is factually supported by the source document
- **Precision**: How directly and accurately the response addresses the query

### Evaluation Scores

| Question | Raw LLM | Prompt-Engineered | RAG |
|----------|---------|-------------------|-----|
| Q1: Authors & publisher | 0.0 / 0.0 | 0.0 / 0.0 | **1.0 / 1.0** |
| Q2: Leadership characteristics | 0.0 / 0.0 | 0.0 / 0.0 | **1.0 / 1.0** |
| Q3: Innovation examples | 0.2 / 0.3 | 0.2 / 0.3 | **0.7 / 0.6** |

(Format: Groundedness / Precision)

### Key Findings

- RAG achieves **perfect scores** on factual/metadata questions where plain LLM scores zero
- Prompt engineering alone does not fix hallucination — retrieved context is essential
- Complex inferential questions score lower (0.7/0.6), suggesting hybrid retrieval and larger k values as next steps

## Sample Q&A

**Query**: "Who are the authors of this article and who published this article?"

**RAG Response**: "The authors of the article are Joel M. Podolny and Morten T. Hansen, and it was published by Harvard Business Review. Source: Harvard Business Review, November–December 2020."

**Raw LLM Response**: "I apologize, but I don't have access to external articles or databases to check specific articles..."

## Data Source

- **Document**: "How Apple is Organized for Innovation" (HBR, Nov–Dec 2020)
- **Authors**: Joel M. Podolny and Morten T. Hansen
- **Format**: PDF, 11 pages
- **Topic**: Organizational culture and business strategy at Apple

## Tech Stack

- **RAG Framework**: LangChain, LangChain Community, LangChain Text Splitters
- **Vector Store**: ChromaDB
- **LLMs**: OpenAI GPT-4o-mini (generation), GPT-4o (evaluation)
- **PDF Processing**: PyMuPDF
- **Tokenization**: tiktoken (`cl100k_base`)
- **Hybrid Retrieval**: BM25Retriever, EnsembleRetriever, rank-bm25
- **Evaluation**: datasets, evaluate
- **Runtime**: Python 3.14

## Getting Started

```bash
git clone https://github.com/ladislav-lettovsky/AI-RAG-Business-Report-Analyst.git
cd AI-RAG-Business-Report-Analyst
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `config.json` file with your API keys:

```json
{
  "OPENAI_API_KEY": "your-openai-api-key"
}
```

Open and run the notebook in Jupyter or Cursor.

## License

This project was developed as part of the UT Austin Postgraduate Program in AI / ML.
