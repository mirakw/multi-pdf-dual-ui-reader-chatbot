# 🌟 Multi-PDF Q&A App with RAG Search 🌟

This project is a **Multi-PDF Q&A Application** that allows users to upload PDF documents, extract and chunk their content, and query them using **Retrieval-Augmented Generation (RAG)**. It is built using **Streamlit** for the UI, **OpenAI's ChatCompletion API** for answering queries, and **SentenceTransformers** for relevant document chunk retrieval.

---

## 🚀 Features
- 🔐 **Admin Page**: Upload PDF files, extract text, and split the content into manageable chunks for search.
- ❓ **Annotator Page**: Query the uploaded PDFs using natural language questions.
- 🔍 **RAG-Enhanced Search**: Retrieve relevant chunks from uploaded PDFs and generate concise answers using OpenAI's ChatCompletion API.

---

## 📁 Project Structure
```
project-folder/
|-- app.py
|-- pdf_reader.py
|-- text_chunker.py
|-- rag_search.py
|-- .env
|-- requirements.txt
|-- README.md
```

---

## ⚙️ Installation and Setup

### 📋 Prerequisites
- Python 3.8+
- pip (Python package manager)

### 📂 Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/multi-pdf-qna-app.git
cd multi-pdf-qna-app
```

### 📦 Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### 🔑 Step 3: Set up environment variables
Create a `.env` file in the project root directory and add your OpenAI API key:
```
OPENAI_API_KEY="your-OpenAI-APIkey"
```

---

## ▶️ How to Run the App
```bash
streamlit run app.py
```
This will launch the app in your default web browser.

---

## 🛠️ Usage

### 🔐 Admin Page
1. Navigate to the **Admin Setup** page using the sidebar.
2. Upload PDF files and let the app extract their content.
3. The content is split into smaller chunks and stored for efficient retrieval.

### ❓ Annotator Page
1. Navigate to the **Annotator Q&A** page using the sidebar.
2. Enter a question related to the uploaded PDFs.
3. The app will retrieve the most relevant chunks and generate an answer using OpenAI's ChatCompletion API.

---

## 📜 File Descriptions

- **app.py**: The main application logic with Streamlit UI.
- **pdf_reader.py**: Extracts plain text from uploaded PDFs using PyMuPDF.
- **text_chunker.py**: Splits long documents into smaller chunks for RAG retrieval.
- **rag_search.py**: Uses SentenceTransformers to retrieve relevant chunks based on the user's query.
- **.env**: Stores the OpenAI API key.
- **requirements.txt**: Lists the Python dependencies for the project.

---

## 📦 Requirements
The following Python libraries are required to run the app (already included in `requirements.txt`):
- streamlit
- openai
- python-dotenv
- sentence-transformers
- pymupdf (PyMuPDF)

To install them manually, run:
```bash
pip install streamlit openai python-dotenv sentence-transformers pymupdf
```

---

## 💡 Example Use Case
- Upload a set of research papers in PDF format.
- Ask questions about key topics in the papers, and get accurate answers with context retrieved directly from the documents.

---

## 🌱 Future Enhancements
- 📚 Large PDF Support: Add chunk-wise processing and support for external vector databases to efficiently handle large PDFs.
- 🔎 Scalable RAG Pipelines: Explore integrating scalable retrieval systems like FAISS or Pinecone.
- 🧩 Improved Chunking Logic: Enhance chunking to better handle structured data, such as tables, headers, and lists.
- 🖼️ Image Processing: Investigate incorporating image data from PDFs (this may be complex but worth exploring).
- 📈 Enhanced Search and Output Quality: Continuously refine the accuracy and relevance of retrieved answers.
- 📑 Page References: Include references to relevant page numbers in responses, ending with “For more information, refer to page X.”
- 💾 Persistent Storage: Store PDF metadata and chunks in a database for long-term use.
- 🔐 User Authentication: Add role-based access control for admins and annotators.
- 📤 Q&A Export: Enable saving and exporting Q&A session results.
  
---

## 👨‍💻 Author
Built by Mira Kapoor Wadehra (https://github.com/mirakw).


