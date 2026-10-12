# 📄 Document Q&A Chatbot

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their contents using natural language. The application retrieves relevant text chunks from the uploaded document and uses Google Gemini to generate context-aware answers.

## ✨ Features

- **PDF Upload:** Upload PDF files through the Streamlit interface.
- **Text Extraction:** Extract document text using LangChain's `PyPDFLoader`.
- **Text Chunking:** Split extracted text into chunks of 1,000 characters with a 200-character overlap.
- **Semantic Search:** Retrieve the five most relevant document chunks for a user's question.
- **AI-Powered Answers:** Generate answers using Google's Gemini language model.
- **Vector Embeddings:** Convert document chunks into vector representations using Google's embedding model.
- **Interactive Chat:** Ask questions through a chat interface and display previous messages during the session.
- **Context-Based Responses:** Instruct the model to acknowledge when an answer cannot be found in the provided context.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface and chat UI |
| LangChain | Document loading, text splitting, and model integration |
| PyPDFLoader | Extract text from PDF documents |
| Google Gemini (`gemini-3.8-flash`) | Generate answers |
| Google Gemini Embeddings (`gemini-embedding-001`) | Generate document embeddings |
| InMemoryVectorStore | Store embeddings and perform similarity search |
| python-dotenv | Load environment variables from `.env` |

## 🏗️ How It Works

1. **Upload:** The user uploads a PDF through Streamlit.
2. **Extract:** `PyPDFLoader` loads the document's pages and extracts their text.
3. **Split:** `RecursiveCharacterTextSplitter` divides the text into chunks of 1,000 characters with 200 characters of overlap.
4. **Embed:** Google Gemini embeddings convert the chunks into vectors.
5. **Store:** `InMemoryVectorStore` stores the document chunks and their embeddings in memory.
6. **Retrieve:** When a question is submitted, similarity search retrieves the top five relevant chunks.
7. **Generate:** The retrieved context and question are passed to Gemini.
8. **Display:** The generated answer appears in the Streamlit chat interface.

## 📂 Project Structure

```text
Document-QnA-Bot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Files excluded from Git
├── sample.pdf              # Sample PDF for testing
├── uploaded_document.pdf   # Temporary uploaded PDF
└── .env                    # API key configuration (not committed)
```

The `.env`, virtual environment, and generated uploaded PDF should remain excluded from Git.

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on your system
- A Google Gemini API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/phanome/Document-QnA-Chatbot.git
cd Document-QnA-Chatbot
```

### 2. Create a virtual environment

On macOS or Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Google Gemini API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 💬 Usage

1. Start the application.
2. Upload a PDF using the **Browse Files** control.
3. Wait for the document processing to finish.
4. Enter a question in the chat input.
5. Read the answer generated using the retrieved document context.
6. Ask additional questions during the same session.

## 🔍 Retrieval Configuration

The application currently uses the following settings:

| Parameter | Value |
|---|---|
| Chunk size | 1,000 characters |
| Chunk overlap | 200 characters |
| Retrieved chunks per question | 5 |
| Chat model | `gemini-3.8-flash` |
| Embedding model | `gemini-embedding-001` |
| Vector store | `InMemoryVectorStore` |

## ⚠️ Limitations

- **Temporary storage:** The vector store exists in memory and is not persisted across application restarts.
- **Single-document workflow:** The application processes one uploaded PDF at a time.
- **API dependency:** Embedding and answer generation require access to Google's API services and are subject to applicable quotas and rate limits.
- **Context limitations:** Answer quality depends on the extracted text and the relevance of retrieved chunks.
- **Scanned PDFs:** Image-only PDFs may require OCR to extract searchable text.
- **Session state:** Chat messages and the vector store are maintained in Streamlit session state.
- **Answer verification:** Generated answers should be checked against the original document when accuracy is important.

## 🚀 Future Improvements

- Add source citations and PDF page references to answers.
- Support multiple PDF uploads.
- Add persistent vector storage using ChromaDB or FAISS.
- Improve error handling for API failures and rate limits.
- Add OCR support for scanned documents.
- Deploy the application publicly using Streamlit Community Cloud.
- Improve chat history management and document replacement.

## 👨‍💻 Author

**Anurag Bais**

GitHub: [@phanome](https://github.com/phanome)

---

*Built with Python, Streamlit, LangChain, and Google Gemini.*
