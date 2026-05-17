# pdf-rag-chatbot
AI-powered multi-document RAG assistant using LangChain, FAISS, HuggingFace embeddings, OpenAI, and Streamlit.

# AI-Powered Multi-Document RAG Assistant 📚

An AI-powered conversational PDF chatbot built using LangChain, FAISS, HuggingFace Embeddings, OpenAI, and Streamlit.

This application allows users to upload multiple PDF documents, process them into vector embeddings, and ask natural language questions about the content using Retrieval-Augmented Generation (RAG).

---

<img width="1919" height="1015" alt="Screenshot 2026-05-17 091135" src="https://github.com/user-attachments/assets/cd0e8644-b995-4358-a3c1-600a770a38f1" />

<img width="1919" height="949" alt="Screenshot 2026-05-17 092033" src="https://github.com/user-attachments/assets/64b147af-7f3e-4af7-841b-ef7c4d5276b2" />

<img width="1919" height="909" alt="Screenshot 2026-05-17 092619" src="https://github.com/user-attachments/assets/f2211e68-2076-45c0-9e8d-962b2a0c039e" />

# Features

* Upload and process multiple PDF documents
* Conversational AI chatbot interface
* Retrieval-Augmented Generation (RAG)
* Semantic search using FAISS vector database
* HuggingFace sentence embeddings
* OpenAI-powered question answering
* Conversational memory for context-aware responses
* Streamlit-based responsive UI

---

# Tech Stack

## Frontend

* Streamlit
* HTML/CSS Templates

## Backend

* Python
* LangChain
* OpenAI API

## AI/ML

* HuggingFace Embeddings
* Sentence Transformers
* FAISS Vector Store

## Document Processing

* PyPDF2

---

# Project Structure

```bash
pdf-rag-chatbot/
│
├── app.py
├── htmlTemplates.py
├── requirements.txt
├── .env
├── README.md
└── assets/
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

---

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Create Environment File

Create a `.env` file in the project root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

---

# How It Works

## Step 1: Upload PDFs

Users upload one or more PDF documents through the Streamlit interface.

## Step 2: Text Extraction

The application extracts text content from uploaded PDF files using PyPDF2.

## Step 3: Chunking

Extracted text is split into smaller chunks for efficient retrieval.

## Step 4: Embedding Generation

HuggingFace sentence-transformer embeddings convert text chunks into vector representations.

## Step 5: Vector Storage

FAISS stores embeddings for fast semantic similarity search.

## Step 6: Conversational Retrieval

LangChain retrieves relevant chunks based on user queries and sends context to the OpenAI model.

## Step 7: AI Response Generation

The chatbot generates contextual responses using Retrieval-Augmented Generation (RAG).

---

# Screenshots

## Main Interface

*Add screenshot here*

## Document Processing

*Add screenshot here*

## Chatbot Responses

*Add screenshot here*

---

# Future Improvements

* Source citation support
* Chat history export
* OCR support for scanned PDFs
* Multi-language document support
* Authentication system
* Cloud deployment
* Docker support
* Streaming AI responses

---

# Deployment Options

This project can be deployed using:

* Streamlit Community Cloud
* HuggingFace Spaces
* Render
* Railway
* AWS EC2

---

# License

This project is licensed under the MIT License.

---

# Author

Srija Gudapati




GitHub: [https://github.com/srija-gudapati](https://github.com/srija-gudapati)

