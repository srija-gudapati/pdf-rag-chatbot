# importing dependencies
import os
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import faiss
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

from htmlTemplates import css, bot_template, user_template


# custom prompt template
custom_template = """
Given the following conversation and a follow up question,
rephrase the follow up question to be a standalone question,
in its original language.

Chat History:
{chat_history}

Follow Up Input: {question}

Standalone question:
"""

CUSTOM_QUESTION_PROMPT = PromptTemplate.from_template(custom_template)


# extracting text from pdfs
def get_pdf_text(docs):
    text = ""

    for pdf in docs:
        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


# splitting text into chunks
def get_chunks(raw_text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(raw_text)

    return chunks


# creating vector store using HuggingFace embeddings + FAISS
def get_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )

    vectorstore = faiss.FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vectorstore


# creating conversation chain
def get_conversationchain(vectorstore):

    llm = ChatOpenAI(
        temperature=0.2
    )

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True,
        output_key='answer'
    )

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,

        retriever=vectorstore.as_retriever(
            search_kwargs={"k": 3}
        ),

        condense_question_prompt=CUSTOM_QUESTION_PROMPT,

        memory=memory,

        return_source_documents=True
    )

    return conversation_chain


# handling user questions
def handle_question(question):

    response = st.session_state.conversation({
        'question': question
    })

    st.session_state.chat_history = response['chat_history']

    # displaying chat history
    for i, msg in enumerate(st.session_state.chat_history):

        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", msg.content),
                unsafe_allow_html=True
            )

        else:
            st.write(
                bot_template.replace("{{MSG}}", msg.content),
                unsafe_allow_html=True
            )

    # displaying source documents
    source_docs = response["source_documents"]

    with st.expander("View Source Chunks"):

        for i, doc in enumerate(source_docs):

            st.write(f"### Source {i+1}")

            st.write(doc.page_content[:500] + "...")

            st.write("---------------------------------")


# main function
def main():

    load_dotenv()

    st.set_page_config(
        page_title="AI-Powered Multi-Document RAG Assistant",
        page_icon="📚"
    )

    st.write(css, unsafe_allow_html=True)

    st.header("AI-Powered Multi-Document RAG Assistant 📚")

    st.caption(
        "Built using LangChain, FAISS, HuggingFace Embeddings, and OpenAI"
    )

    # checking OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):

        st.error("Please add your OPENAI_API_KEY in the .env file")

        st.stop()

    # session states
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # user input
    question = st.text_input(
        "Ask a question about your documents:"
    )

    if question:

        if st.session_state.conversation is None:

            st.warning("Please upload and process documents first.")

        else:
            handle_question(question)

    # sidebar
    with st.sidebar:

        st.subheader("Your Documents")

        docs = st.file_uploader(
            "Upload your PDF files here",
            accept_multiple_files=True
        )

        if st.button("Process Documents"):

            if docs:

                with st.spinner("Processing documents..."):

                    # extracting raw text
                    raw_text = get_pdf_text(docs)

                    # splitting into chunks
                    text_chunks = get_chunks(raw_text)

                    # creating vector store
                    vectorstore = get_vectorstore(text_chunks)

                    # creating conversation chain
                    st.session_state.conversation = get_conversationchain(
                        vectorstore
                    )

                    st.success("Documents processed successfully!")

            else:
                st.warning("Please upload at least one PDF file.")


# running app
if __name__ == '__main__':
    main()
