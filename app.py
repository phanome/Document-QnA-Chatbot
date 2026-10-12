from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_community.vectorstores import InMemoryVectorStore
import streamlit as st
from time import sleep

llm=ChatGoogleGenerativeAI(model="gemini-3.8-flash")

if "vector_db" not in st.session_state:
    st.session_state.vector_db=None

if "messages" not in st.session_state:
    st.session_state.messages=[]

def document_process(path):
    ## document loading
    loader = PyPDFLoader(path)
    docs=loader.load()


    ## splitting
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200)
    docs=splitter.split_documents(docs)
   

    ## embedding and vector storage
    embeddings=GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    vector_db=InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)
    st.session_state.vector_db=vector_db
    st.session_state.document_uploaded=True






#######
#######
#######


st.subheader(" Document QnA Chatbot")

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded=False

# document upload UI
if not st.session_state.document_uploaded:
    file = st.file_uploader(label="Browse Files", type="pdf")

    if file:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())

        with st.spinner("Processing document..."):
           document_process("./uploaded_document.pdf")
        st.markdown("Document processed successfully...")
        sleep(2)
        st.rerun()


if st.session_state.document_uploaded and st.session_state.vector_db is not None:
    
    for oneMessage in st.session_state.messages:
        role=oneMessage["role"]
        content=oneMessage["content"]
        st.chat_message(role).markdown(content)
        
    query=st.chat_input("Ask anything about the document...")
    if query:
        st.session_state.messages.append({"role":"user","content":query})   



        st.chat_message("user").markdown(query)
        documents=st.session_state.vector_db.similarity_search(query,k=5)
        context=""
        for doc in documents:
            context+=doc.page_content+"\n\n"
        prompt=f"""
                You are a helpful assistant that answers questions based on 
                the context provided.
                Context:{context}
                Question: {query}
                If the answer is not present in the context,
                        say you cannot find it in the document."""
        result=llm.invoke(prompt)
       # print(result.content)
        #st.chat_message("ai").markdown(result.content)
        st.session_state.messages.append({"role":"ai","content":result.content}) 
        if isinstance(result.content, str):
            answer = result.content
        else:
            answer = "\n".join(
        item["text"]
        for item in result.content
        if isinstance(item, dict) and item.get("type") == "text"
    )

        st.markdown(answer)





# chat UI